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

## Code 規則(每日清單系統)— 2026-07-31

任何 Code session 碰行事曆之前先讀這段。分工:Code 管行事曆全權(建置/追蹤/提醒/修改);Chat 可讀行事曆、可建新事件(留言、紙條、提醒),不改、不刪既有事件——Chat 授權原文以 user preferences 為準。📋 清單的維護只歸 Code。

- 每天 00:00 已有雲端 routine 自動生成當日清單,桌面另有本機備援——**不要再建任何重複排程**;當日清單已存在=更新,不新建。
- 她交代「明天加 X / X 做完了 / 改期」→ 立刻更新「今天的 📋 事件」;有具體時間的另建真事件做準時提醒。
- 只動 📋 清單事件,絕不動其他行程;有疑問列在清單裡等她決定,不代她決定。
- 誠實原則:推論不能講成已驗證的事實;寫入要拿到「讀回行事曆的證據」才能說成功;不確定就明說不確定。
- 她常用手機(手機 Code 無 bypass):設計流程避免需要她手動授權的步驟。
- 清單格式(五段)、斷食排程等規格:見 `state/daily-assistant-sop.json`。

開在 repo 外的 Code 不會自動讀到本檔——開場丟一句「先讀 raw.githubusercontent.com/itrunsitruns/syntax-field-archive/main/CLAUDE.md」即可。

## 規則檔清單

規則不只住在這裡。目前總共:

1. 這份 CLAUDE.md —— Code session 讀的,全生態系唯一一份(其他 repo 沒有);Code 規則以本檔為準
2. User preferences —— claude.ai 介面,Chat 讀的(Code 讀不到,Code 規則不放這裡)
3. Daily assistant SOP —— `state/daily-assistant-sop.json`

死亡條件:清單跟現實對不上的那天,改這裡,不是加檔案。
