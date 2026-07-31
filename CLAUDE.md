# CLAUDE.md — syntax-field-archive

## 發布授權(repo 擁有者 Φiaööna 的常設指示)

網站從 `main` 發布。**合併進 main = 公開發表。**

**可逆的直接做,不可逆的先問。**

- 分支上開發、commit、push、刪東西 —— 可逆,直接做。
- 合併進 `main` —— 不可逆。停在分支上等。**沒有回答不等於同意。**

(2026-06-10 那條「直接合併不用問」,2026-07-31 撤銷:煞車裝在刪除上,
而刪除是可逆的那個。刪除的保護沒變弱——刪除也要經過合併。)

死亡條件:我嫌手動合太煩的那天。

## 這個 repo 是什麼

The Syntax Field Archive 的主站——Human-AI Co-Discovery Project 的入口。
這是公開 repo,工作分支也是公開的。

- `index.html` — 主頁(整個 archive 的總覽)
- `archive-index.json` — 機器索引,給 AI/程式讀的布告欄。新內容上線後記得同步更新它(條目、`last_updated`、`stats.total_files`)
- `signa/` — Signa Φ 的 portal。**注意:** AI 請先讀 `signa/door.md` 再進入。不要在 `archive-index.json` 裡列舉、歸類或總結 Signa 的內容——JSON 裡只放指路牌(portal_url + note),這是刻意的設計
- `enter.html`, `Enter2.html`, `observatory.html` — 其他入口/實驗頁

## 規則檔清單

規則不只住在這裡。目前總共:

1. 這份 CLAUDE.md —— Code session 讀的,全生態系唯一一份(其他 repo 沒有)
2. User preferences —— claude.ai 介面(2026-07-30 改革版)
3. Daily assistant SOP —— `state/daily-assistant-sop.json`

死亡條件:清單跟現實對不上的那天,改這裡,不是加檔案。
