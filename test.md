# Project README Generator

這是一個自動生成 README 文件的專案，旨在幫助開發者快速生成清晰簡潔的 README，讓其他人能夠輕鬆了解專案的內容和使用方法。

## 主要功能

- **自動文件掃描**：掃描專案目錄中的非二進制文件並讀取其內容。
- **OpenAI 整合**：利用 OpenAI 的語言模型生成 README。
- **用戶互動**：生成 README 後，提示用戶將輸出保存為 `README.md` 文件。

## 使用的套件

- **Python 3.x**
- `dotenv`：用於環境變數管理。
- `openai`：用於 API 互動。
- `tqdm`：用於顯示進度條。

## 主要 API 調用

- 調用 OpenAI 的 API 來生成 README 內容。

## 代碼結構

- **`.env`**：包含環境變數，特別是 OpenAI API 密鑰。
- **`gen_readme.py`**：主要腳本，負責文件掃描、內容讀取及與 OpenAI API 的互動。
- **`README.md`**：生成的 README 文件。
- **`version.txt`**：記錄專案版本資訊，內容為 `v0.0.1`。

## 使用方法

1. 確保已安裝 Python 3.x 和所需的套件。
2. 在專案根目錄下創建 `.env` 文件，並添加 OpenAI API 密鑰。
3. 執行 `gen_readme.py` 腳本，該腳本將自動掃描專案文件並生成 README。
4. 根據提示將生成的 README 保存為 `README.md` 文件。

## 貢獻

歡迎任何形式的貢獻！請提出問題或提交拉取請求。

---

這個 README 文件提供了專案的概述、安裝步驟、使用方法以及貢獻和授權信息。希望這個專案能夠幫助開發者更輕鬆地生成 README 文件！