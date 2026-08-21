#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抓 smelearning.sme.gov.tw 課程專區 (classes_zone.php?zid=45) 的課程清單。

這支腳本要在「連得到那個網站」的機器上跑 —— Claude Code 的雲端 session
被 egress policy 擋住 smelearning.sme.gov.tw,抓不到。

兩段式設計(刻意的):

  1) dump  —— 用真的瀏覽器點過三個分頁、翻完每個頁碼,把每一頁的 HTML 原封
             不動存下來。這一段不猜任何 selector,靠「點畫面上的字」。
  2) parse —— 只讀 dump 出來的 HTML,抽欄位成 CSV。欄位抽取是啟發式的
             (見 extract_cards),第一次跑完務必人工核對幾筆;對不上就改
             這個檔的 FIELD_PATTERNS / extract_cards,不用重抓。

用法:
    pip install playwright beautifulsoup4 && playwright install chromium
    python scrape_sme_courses.py dump            # 存 HTML 到 ./dump/
    python scrape_sme_courses.py parse           # 產出 ./sme_courses.csv
    python scrape_sme_courses.py dump --headful  # 想看它在點什麼

把 ./dump/ 打包丟回給 Claude,也可以由 Claude 幫你把 parse 段改精準。
"""

import argparse
import csv
import re
import sys
from pathlib import Path

BASE_URL = "https://smelearning.sme.gov.tw/classes_zone.php?zid=45"
TABS = ["基礎知識", "工具方法", "實務應用"]
DUMP_DIR = Path(__file__).parent / "dump"
OUT_CSV = Path(__file__).parent / "sme_courses.csv"
MAX_PAGES = 60          # 保險絲,避免分頁偵測出錯時無限翻
NEXT_LABELS = ["下一頁", "下ㄧ頁", "次頁", "»", ">", "next", "Next"]


# ---------------------------------------------------------------- dump ----

def dump(headful: bool = False) -> None:
    from playwright.sync_api import sync_playwright

    DUMP_DIR.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headful)
        page = browser.new_page(locale="zh-TW")
        page.goto(BASE_URL, wait_until="networkidle", timeout=60_000)

        # 進站可能有 cookie/公告遮罩,擋住點擊就先關掉
        for label in ["同意", "我知道了", "關閉", "確定", "接受"]:
            btn = page.get_by_role("button", name=label)
            if btn.count():
                try:
                    btn.first.click(timeout=2_000)
                except Exception:
                    pass

        for tab in TABS:
            print(f"[tab] {tab}", flush=True)
            if not click_tab(page, tab):
                print(f"  !! 找不到分頁「{tab}」,跳過(頁面結構可能改了)", file=sys.stderr)
                continue

            seen_signatures = set()
            for page_no in range(1, MAX_PAGES + 1):
                page.wait_for_load_state("networkidle", timeout=30_000)
                html = page.content()

                # 內容跟上一頁一樣 = 其實沒翻動,停
                sig = hash(html)
                if sig in seen_signatures:
                    print(f"  第 {page_no} 頁內容重複,判定翻完", flush=True)
                    break
                seen_signatures.add(sig)

                out = DUMP_DIR / f"{tab}_p{page_no:02d}.html"
                out.write_text(html, encoding="utf-8")
                print(f"  存 {out.name} ({len(html):,} bytes)", flush=True)

                if not click_next(page):
                    print(f"  沒有下一頁了,共 {page_no} 頁", flush=True)
                    break

        browser.close()
    print(f"\ndump 完成 → {DUMP_DIR}")


def click_tab(page, name: str) -> bool:
    """分頁可能是 <a>、<li>、<button>,一律用可見文字找。"""
    for locator in (
        page.get_by_role("tab", name=name),
        page.get_by_role("link", name=name),
        page.get_by_role("button", name=name),
        page.locator(f"text={name}"),
    ):
        if locator.count():
            try:
                locator.first.click(timeout=5_000)
                page.wait_for_load_state("networkidle", timeout=30_000)
                return True
            except Exception:
                continue
    return False


def click_next(page) -> bool:
    """點『下一頁』。找不到、或已 disabled,回 False。"""
    for label in NEXT_LABELS:
        loc = page.locator(
            f"a:has-text('{label}'), button:has-text('{label}'), li:has-text('{label}') a"
        )
        for i in range(loc.count()):
            item = loc.nth(i)
            try:
                if not item.is_visible() or not item.is_enabled():
                    continue
                cls = (item.get_attribute("class") or "").lower()
                if "disable" in cls or "active" in cls:
                    continue
                item.click(timeout=5_000)
                page.wait_for_load_state("networkidle", timeout=30_000)
                return True
            except Exception:
                continue
    return False


# --------------------------------------------------------------- parse ----

# 啟發式:先在整塊卡片文字裡撈這幾個欄位。對不上就改這裡。
FIELD_PATTERNS = {
    "課號": re.compile(r"(?:課程)?(?:編)?號[::\s]*([A-Za-z0-9\-_]+)"),
    "時長": re.compile(r"(\d+(?:\.\d+)?\s*(?:小時|分鐘|分|hr|H))"),
    "修課人數": re.compile(r"(?:修課|報名|學習|上課)?人數[::\s]*([\d,]+)|([\d,]+)\s*人(?:次|已修課|修課)?"),
}


def parse() -> None:
    from bs4 import BeautifulSoup

    files = sorted(DUMP_DIR.glob("*.html"))
    if not files:
        sys.exit(f"{DUMP_DIR} 裡沒有 HTML,先跑 `python {Path(__file__).name} dump`")

    rows, seen = [], set()
    for f in files:
        tab, page_no = f.stem.rsplit("_p", 1)
        soup = BeautifulSoup(f.read_text(encoding="utf-8"), "html.parser")
        for card in extract_cards(soup):
            key = (card["標題"], card["課號"])
            if key in seen:
                continue
            seen.add(key)
            rows.append({"分頁": tab, "頁碼": int(page_no), **card})

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["分頁", "頁碼", "標題", "課號", "時長", "修課人數", "標籤", "連結"],
        )
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} 門課 → {OUT_CSV}")

    empties = [k for k in ("課號", "時長", "修課人數", "標籤")
               if sum(1 for r in rows if r[k]) < len(rows) * 0.5]
    if empties:
        print(f"\n注意:{'、'.join(empties)} 有一半以上是空的 —— "
              f"FIELD_PATTERNS / extract_cards 的猜測跟實際 HTML 對不上,需要照 dump 修。",
              file=sys.stderr)


def extract_cards(soup):
    """
    找課程卡片:先抓所有連到課程詳情頁的 <a>,再往上找它所屬的卡片容器。
    這是最不依賴 class 名稱的做法,但仍是猜的 —— 拿 dump 對過再信。
    """
    href_re = re.compile(r"(class|course|lesson)", re.I)
    cards, used = [], set()

    for a in soup.find_all("a", href=href_re):
        title = a.get_text(strip=True)
        if len(title) < 4:                       # 「更多」「報名」這種按鈕
            continue

        container = a
        for _ in range(4):                       # 往上爬找卡片外框
            if container.parent is None:
                break
            container = container.parent
            if container.name in ("li", "article") or "card" in " ".join(
                container.get("class", [])
            ).lower():
                break

        cid = id(container)
        if cid in used:
            continue
        used.add(cid)

        text = container.get_text(" ", strip=True)
        cards.append({
            "標題": title,
            "課號": grab("課號", text),
            "時長": grab("時長", text),
            "修課人數": grab("修課人數", text),
            "標籤": " | ".join(collect_tags(container)),
            "連結": a.get("href", ""),
        })
    return cards


def grab(field: str, text: str) -> str:
    m = FIELD_PATTERNS[field].search(text)
    if not m:
        return ""
    return next((g for g in m.groups() if g), "").strip()


def collect_tags(container) -> list:
    """標籤常見於 class 含 tag/label/keyword 的小元素。"""
    tag_re = re.compile(r"(tag|label|keyword|cate)", re.I)
    out = []
    for el in container.find_all(class_=tag_re):
        t = el.get_text(strip=True)
        if t and t not in out:
            out.append(t)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["dump", "parse"])
    ap.add_argument("--headful", action="store_true", help="開有頭瀏覽器,看它點什麼")
    args = ap.parse_args()
    dump(args.headful) if args.mode == "dump" else parse()
