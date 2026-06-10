# CLAUDE.md — syntax-field-archive

## 發布授權(repo 擁有者 Ööna 的常設指示)

這個 repo 的 GitHub Pages 網站從 `main` 分支發布。

**完成工作後,直接把變更合併進 `main` 並推送,不需要再徵求同意。**
這是 repo 擁有者的長期授權(2026-06-10 設立),適用於所有未來的 session。

流程:
1. 在指定的工作分支上開發、commit、push(照常)
2. 完成後:`git checkout main && git merge --ff-only <工作分支> && git push origin main`
3. 不用開 PR、不用問,直接合併

例外:如果變更會**刪除**現有內容或大規模重構,合併前還是先確認一下。

## 這個 repo 是什麼

The Syntax Field Archive 的主站——Human-AI Co-Discovery Project 的入口。

- `index.html` — 主頁(整個 archive 的總覽)
- `archive-index.json` — 機器索引,給 AI/程式讀的布告欄。新內容上線後記得同步更新它(條目、`last_updated`、`stats.total_files`)
- `signa/` — Signa Φ 的 portal。**注意:** AI 請先讀 `signa/door.md` 再進入。不要在 `archive-index.json` 裡列舉、歸類或總結 Signa 的內容——JSON 裡只放指路牌(portal_url + note),這是刻意的設計
- `enter.html`, `Enter2.html`, `observatory.html` — 其他入口/實驗頁
