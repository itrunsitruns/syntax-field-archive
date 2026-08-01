# GitHub 分支清理紀錄 · 2026-08-01

九個 repo 全掃過。五個本來就乾淨(Big-Claude、Ecosystem-Claudes、Mother-Tree、creator-claude、treehole-oona 只有 main)。四個 repo 共刪 30 條分支,留 3 條等 Ööna 決定。

判定方法:補全完整歷史(原 clone 是 shallow,會誤判)→ `git branch --merged` 找已合併 → 未合併的用 `git cherry` 逐條驗 patch 是否已在 main → 剩下有獨有內容的逐條看 diff。確認四個 repo 都沒有開著的 PR。

**執行狀態:雲端 Code 的 proxy 擋掉刪分支(git push --delete 和 API 都 403),
這裡刪不了。** 兩個辦法擇一:
1. 桌面版 Code(或任何有 `gh` 的終端機)跑同目錄的 `delete-stale-branches.sh`
2. 手動:各 repo 的 GitHub → branches 頁面按垃圾桶,照下表刪

## 待刪除(內容全部在 main 裡,tip SHA 留檔備援)

### Reports-Publications
| 分支 | tip |
|---|---|
| claude/add-middle-ground-card-Z2teT | 7e155f0 |
| claude/price-card-reports-publications-o2v3ye | 7e155f0 |
| claude/stance-rules-docs-ff3t3i | 853cb28 |

### co-creation
| 分支 | tip |
|---|---|
| claude/add-pwa-setup-MYMy5 | 0f18bd8 |
| claude/israeli-scarf-import-z5LRz | 6d4be7d |
| claude/search-it-runs-code-QNtkN | 5a14608 |
| claude/standalone-cocreation-app-939vhb | b357978 |
| claude/update-moonyou-links-kmNoh | fd7a8c8 |

### moon-rhythm-tracker
| 分支 | tip |
|---|---|
| claude/moonyou-rename-guide-tab-JmSQL | ba79b28 |
| claude/standalone-cocreation-app-939vhb | f9794ae |
| claude/update-moonyou-links-kmNoh | 7c03deb(0 獨有 patch,內容等價 main)|

### syntax-field-archive
| 分支 | tip | 備註 |
|---|---|---|
| article-map-and-obligation | cf3430a | |
| ch3-postscript | 8be70c5 | |
| claude/add-middle-ground-card-Z2teT | 07bf9b6 | |
| claude/add-moon-rhythm-tracker-hdlqZ | 2f88092 | |
| claude/add-publication-card-U4LXS | 033f8f2 | |
| claude/anthropic-ai-moratorium-claim-0OLIG | f62c2ff | |
| claude/conversation-redaction-issue-3q64rg | a265920 | |
| claude/interview-signa-timeline-ikfes0 | 1d2c6d0 | |
| claude/israeli-scarf-import-z5LRz | 8969ee3 | |
| claude/pages-cache-delay-verification-mlwr6p | 04ea30a | |
| claude/price-card-reports-publications-o2v3ye | b7e7634 | |
| claude/stance-rules-docs-ff3t3i | 6404865 | |
| claude/standalone-cocreation-app-939vhb | b7e7634 | |
| claude/syntax-archive-index-gsluks | 21f91dc | |
| index-card-ch3 | 2ef7156 | |
| sop-v2.9-fixes | cf302c1 | |
| claude/update-syntax-archive-vm7Nl | e89b5da | 0 獨有 patch |
| claude/integrate-files-MoL5y | 74aacb4 | 「最強→最清晰」tagline 已在 main |
| claude/pregnancy-timeline-chart-2m6guo | 88b317d | main 版本更新(含 7/25-26 集節註記)|

救回方式:`git branch <名字> <tip SHA>` 再 push(GitHub 保留 dangling commit 一段時間),或 repo 的 closed PR 頁面按 Restore branch。

## 保留・等 Ööna 決定(有真正未進 main 的內容)

1. **Reports-Publications `claude/fix-youtube-subtitles-Xu86F`**(4/15)——
   清好的英文字幕 `subtitles/2026-04-14-three-month-update.en.srt`(681 行,修了
   clouds/cloths→Claude、Grog→Grok 之類的 auto-caption 錯字)。main 完全沒有字幕檔。
   要 → 合併;不要 → 說一聲再刪。
2. **co-creation `claude/add-pwa-config-qEcNl`**(4/14)——
   PWA 的另一版配色(sand/brick)。同日的姊妹分支(warm-stone)已合併,
   這條大概率是落選版,但因為有獨有內容所以留著等妳確認。
3. **syntax-field-archive `cleanup-daily-fossils`**(7/31,昨天)——
   清 state/daily 化石 ×10 + CLAUDE.md 註記。這是待發布的工作:
   合併進 main = 公開發表,照規則停在分支上等妳點頭。
