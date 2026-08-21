# SME 課程專區抓取(zid=45)

目標:`smelearning.sme.gov.tw/classes_zone.php?zid=45` 的
**基礎知識／工具方法／實務應用** 三個分頁,翻完所有頁碼,
每門課抓 標題、課號、時長、修課人數、標籤,存成一個 CSV。

## 為什麼是腳本不是 CSV

Claude Code 的雲端 session 出不去這個網域 —— egress proxy 對
`smelearning.sme.gov.tw:443` 的 CONNECT 回 403(policy denial),
`curl` 和 WebFetch 都一樣。這台機器連 `example.com` 也連不到,
是整體封鎖,不是這個站被特別擋。所以資料要在你自己的機器上抓。

要讓雲端 session 自己抓,得在建 environment 時放寬 network policy:
https://code.claude.com/docs/en/claude-code-on-the-web

## 怎麼跑

```bash
pip install playwright beautifulsoup4
playwright install chromium

python scrape_sme_courses.py dump      # 點過三個分頁、翻完頁碼,存 HTML 到 ./dump/
python scrape_sme_courses.py parse     # 讀 ./dump/ 產出 ./sme_courses.csv
```

想看它在點什麼:`python scrape_sme_courses.py dump --headful`

## 兩段式是刻意的

`dump` 段只靠「點畫面上看得到的字」(分頁名、下一頁),不猜 CSS class,
所以就算網站改版也大致還能翻頁。

`parse` 段的欄位抽取是**猜的** —— 我沒看過那個站的真實 HTML,
`FIELD_PATTERNS` 和 `extract_cards()` 是照台灣政府課程網站的常見寫法推的。
第一次跑完:

- 人工核對幾筆 CSV 跟網頁上的內容;
- 若某欄一半以上是空的,`parse` 會在 stderr 直接警告你;
- 對不上就改這個檔的正則/選擇器,**不用重抓**(HTML 已經在 `./dump/`)。

或者把 `./dump/` 丟回給 Claude,由它照真實 HTML 把 parse 段改精準。

## 輸出欄位

`分頁, 頁碼, 標題, 課號, 時長, 修課人數, 標籤, 連結` — UTF-8 with BOM(Excel 直接開)。
