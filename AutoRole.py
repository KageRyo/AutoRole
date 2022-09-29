#導入 Discord.py
from email import message
import discord

import RoleName
import TOKEN

intents = discord.Intents.default()
intents.message_content = True
#client 是我們與 Discord 連結的橋樑
bot = discord.Client(intents=intents)

#調用 event 函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    #確認連結TOKEN的BOT是否有誤
    print('目前登入身份：', bot.user)
    #機器人的遊戲狀態，想設什麼都可以
    game = discord.Game('正在採琉連')
    #機器人的在線狀態
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    #如果包含 peko，機器人回傳 好油哦
    if message.content == "peko":
        await message.channel.send("好油哦")

@bot.event
#當有成員加入（DC群）時
async def on_member_join(member):
    #給予加入DC群的成員 RoleName.name 的身分組
    role = discord.utils.get(member.guild.roles, name=RoleName.name)
    await member.add_roles(role)
    #當然這也可以打 await message.channel.send("歡迎加入") 等做出加入DC時發送的訊息
    #await message.channel.send("歡迎加入(XXX)DC群")

bot.run(TOKEN.TOKEN) #TOKEN 袃 Discord Developer 的 BOT 頁面