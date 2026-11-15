---
name: airbnb
description: Φiaööna 說「Airbnb」「看信」「房客」「訂房」時用。讀 Gmail 裡 Airbnb 的信,整理成待辦,照接單規則擬回覆草稿(只存草稿,不寄),更新 state/work.json 的 Airbnb 卡。
---

# Airbnb 信件整理 · 工作員工 v0(2026-11-09)

這是 Φiaööna 的「總管」底下第一個員工。觸發就做完下面五步,不問要不要。

## 1. 讀信
Gmail 搜 `from:airbnb.com newer_than:14d`(她說時間就照她的)。
每個 thread 用 `get_thread` + `PLAIN_TEXT` 讀全文。注意:信裡只有房客那邊的話,她回的不在信箱。

## 2. 分三堆
- **要回的**:inquiry / request / 房客訊息,看 Airbnb 給的回覆期限(「Respond by …」)。
- **要知道的**:入住提醒、退房、匯款、共同房東邀請、政策變更。
- **可忽略**:行銷信(discover@airbnb.com 多半是)。

## 3. 套規則(以 state/now.md「Airbnb 接單規則」為準,那裡是正本)
目前三條:30 天起;零評價不預先批准、讓對方送訂房申請、先問清楚目的與人數;只走 Airbnb;對房子有超出住宿的興趣就問一次。
評價數看信裡「Identity verified · N reviews」那行,沒寫 N 就當零。

## 4. 擬草稿
用 `create_draft` + `replyToMessageId` 回到該封信(Airbnb 支援直接回信)。
用房客的語言寫。**只存草稿,永遠不寄。** 她在手機 Gmail 草稿匣看、改、寄。
草稿語氣:她的,不是客服的。短、暖、問題編號。簽名 Ööna(Airbnb 上她用這個名字)。

## 5. 更新工作板
改 `state/work.json` 裡 `airbnb_2f` / `airbnb_3f` 的 now / next / waiting。
不寫房客姓名,寫「一組詢問 2027/3–4 兩個月、零評價」這種。
commit、push 分支,不合併。

## 回報格式(給她看的,五行以內)
每間一行:誰在等她、期限、草稿存了沒。最後一行:這則最重要的是:X。

## 不做
不寄信、不預先批准、不改價、不接受或拒絕任何訂單。這些都是她按。
