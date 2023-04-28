# DiscordAutoRoleBot
Discord 自動分配身份組機器人

本程式使用 Python 語言和 [Discord.py](https://discordpy.readthedocs.io/en/stable/) 模組來實現。該機器人可以在新成員加入 Discord 群時自動給予指定的身份組。

## 使用方法

1. 在 Discord 開發者頁面中建立一個新的機器人，獲取其 TOKEN。
2. 將 TOKEN 和身份組 ID 或名稱添加到 `config.py` 文件中，以便在程式碼中調用。
3. 運行 `bot.py` 文件，啟動機器人。
4. 當有成員加入 Discord 群時，機器人會自動給予指定的身份組。

您也可以編輯程式碼，使機器人發送歡迎訊息或其他訊息給新成員。具體的編輯方式可以參考 `bot.py` 文件中的註釋。

## 需要的 Python 環境

- Python 3.7 或更高版本
- Discord.py 1.7.2 或更高版本

## 注意事項

- 在將程式碼部署到公共伺服器或私人伺服器之前，請務必將 TOKEN 隱藏起來，以免被他人拿到。
- 請務必確保程式碼中的身份組 ID 或名稱是存在於 Discord 群中的有效身份組。
- 如果機器人無法正常運行，請確保已經在 Discord 開發者頁面中啟用了相應的 Intents。
- 本程式僅供學習和測試使用，請勿濫用或用於商業用途。

## 參考資料

- [Discord 開發者文件](https://discord.com/developers/docs/)
- [Discord.py 文檔](https://discordpy.readthedocs.io/en/stable/)
