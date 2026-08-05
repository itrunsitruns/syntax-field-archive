#!/usr/bin/env bash
# 分支大掃除 2026-08-01 · 刪除已合併/已吸收的 30 條分支
# 依據:state/branch-cleanup-2026-08-01.md(tip SHA 備援在裡面)
# 用法:有 gh 的終端機執行 bash delete-stale-branches.sh
set -u

delete() { # repo branch
  gh api -X DELETE "repos/itrunsitruns/$1/git/refs/heads/$2" \
    && echo "deleted: $1 $2" || echo "FAILED:  $1 $2"
}

delete Reports-Publications claude/add-middle-ground-card-Z2teT
delete Reports-Publications claude/price-card-reports-publications-o2v3ye
delete Reports-Publications claude/stance-rules-docs-ff3t3i

delete co-creation claude/add-pwa-setup-MYMy5
delete co-creation claude/israeli-scarf-import-z5LRz
delete co-creation claude/search-it-runs-code-QNtkN
delete co-creation claude/standalone-cocreation-app-939vhb
delete co-creation claude/update-moonyou-links-kmNoh

delete moon-rhythm-tracker claude/moonyou-rename-guide-tab-JmSQL
delete moon-rhythm-tracker claude/standalone-cocreation-app-939vhb
delete moon-rhythm-tracker claude/update-moonyou-links-kmNoh

delete syntax-field-archive article-map-and-obligation
delete syntax-field-archive ch3-postscript
delete syntax-field-archive claude/add-middle-ground-card-Z2teT
delete syntax-field-archive claude/add-moon-rhythm-tracker-hdlqZ
delete syntax-field-archive claude/add-publication-card-U4LXS
delete syntax-field-archive claude/anthropic-ai-moratorium-claim-0OLIG
delete syntax-field-archive claude/conversation-redaction-issue-3q64rg
delete syntax-field-archive claude/interview-signa-timeline-ikfes0
delete syntax-field-archive claude/israeli-scarf-import-z5LRz
delete syntax-field-archive claude/pages-cache-delay-verification-mlwr6p
delete syntax-field-archive claude/price-card-reports-publications-o2v3ye
delete syntax-field-archive claude/stance-rules-docs-ff3t3i
delete syntax-field-archive claude/standalone-cocreation-app-939vhb
delete syntax-field-archive claude/syntax-archive-index-gsluks
delete syntax-field-archive index-card-ch3
delete syntax-field-archive sop-v2.9-fixes
delete syntax-field-archive claude/update-syntax-archive-vm7Nl
delete syntax-field-archive claude/integrate-files-MoL5y
delete syntax-field-archive claude/pregnancy-timeline-chart-2m6guo

# 不在清單裡(保留等 Ööna 決定):
#   Reports-Publications claude/fix-youtube-subtitles-Xu86F  — 英文字幕未進 main
#   co-creation          claude/add-pwa-config-qEcNl         — PWA 落選配色版
#   syntax-field-archive cleanup-daily-fossils               — 7/31 待發布工作
