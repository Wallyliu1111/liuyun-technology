# 琉雲科技｜LIUYUN TECHNOLOGY 多頁網站 prototype

這是一個以 buyersline.com.tw 的公開資訊架構與服務頁節奏為參考、重新設計為琉雲科技品牌的**多頁網站**，不是把 `web_path.html` 當成單頁站。

GitHub Pages：<https://wallyliu1111.github.io/liuyun-technology/>

## 多頁 routes

- `index.html`：首頁
- `web_path.html`：高CP網站設計／設計報價
- `shop_path.html`：購物網站設計
- `brand-web.html`：B2C品牌網站
- `b2b.html`：B2B品牌網站
- `system.html`：客製程式網站
- `cis-logo.html`：CIS／Logo設計
- `catalog-design.html`：型錄DM設計
- `marketing.html`：數位網路行銷
- `about.html`：公司簡介
- `works.html`：網頁設計實績
- `food.html`：食品餐旅場景
- `architecture.html`：建築建材場景
- `technology.html`：科技電子場景
- `knowledge.html`：網頁設計學堂
- `marketing-knowledge.html`：網路行銷學堂
- `contact.html`：索取報價
- `works/<case-id>.html`：17 個案例 detail page

完整清單在 `routes.json`，共 33 個 page-data routes；加上首頁與 17 個 detail routes，瀏覽器驗收共跑 34 個 URL。

## 案例分類

案例分類改成以動畫畫面實際可辨識的用途為準：

- AI／科技產品
- B2B SaaS
- 心理健康
- 創意設計
- 跨境物流
- 美容電商
- 網路商城
- 食品餐旅
- 攝影內容
- 概念設計

不再把沒有出現的餐飲、建築或商品內容硬套到動畫上；畫面不足以判斷實際產業時，使用「概念設計」而不是編造客戶場景。

## 開啟

```bash
cd /Users/laina/.hermes/profiles/sales/workspace/liuyun-technology
python3 -m http.server 8765
```

若 8765 已被既有 server 使用，不要重開；直接開啟：

```bash
open http://127.0.0.1:8765/
```

## 主要檔案

- `index.html` / `styles.css` / `app.js`：首頁
- `site-data.js`：多頁內容資料
- `subpage.js` / `subpage.css`：共用內頁 renderer 與樣式
- `generate_subpages.py`：產生 33 個資料頁與 17 個案例 detail page
- `cases.js` / `cases.json`：17 個 motion 案例 metadata
- `nav.js`：首頁與所有內頁共用 Header、網站設計／網頁作品／知識學堂 dropdown 與手機點擊展開
- `routes.json`：route 清單
- `assets/media/`：本地 MotionSites archive 預覽素材

## 完整 BuyersLine snapshot

v2 全站掃描在：

```text
/Users/laina/.hermes/profiles/sales/workspace/buyersline_full_snapshot_v2/
```

實際結果：

```text
381 個 discovered/crawled pages
379 個 HTTP 200
377 個 unique internal links
1,273 個 unique image URLs
0 個 HTML <video> tags
```

`pages.jsonl` 保存每頁 URL、title、headings、正文、內部連結、圖片、CSS、JS 與 HTML 路徑；`pages/` 保存原始 HTML。中文與空白 URL 已 percent-encode，暫時性 503 已重試。

## 邊界

這不是百邇來網站的逐字逐碼複製。保留的是公開資訊架構、頁面分層、SEO 主題與服務導覽邏輯；logo、品牌、程式碼、案例素材與頁面視覺改為琉雲科技版本。正式商用前，請確認本地動畫預覽素材授權，並把報價表單接上正式 CRM／表單端點。

本 repo 的 MotionSites 動畫為公開預覽素材展示；公開 Pages 主要用於 prototype／作品展示，正式商用前仍需逐項確認素材授權。

## 驗證

- 多頁 browser QA：34/34 routes 通過，Header signature 只有 1 組
- desktop/mobile 首頁：6 張精選案例、5 個 video、0 個真正 failed request、0 個 console error
- 作品頁：17 個案例；首頁明確保留 6 個精選
- 食品餐旅篩選：2 張相關案例；食品頁只展示食品／咖啡相關案例
- reduced motion：首頁 reveal 元件直接顯示
- 內頁 modal：開啟／關閉通過
- desktop dropdown：初始關閉、滑鼠移入開啟、移出關閉
- mobile menu：開啟、`aria-expanded=true`、網站設計 dropdown 點擊展開 7 個子項
