import datetime as dt
import time
import json
import asyncio
import os
import shutil
from telebot.async_telebot import AsyncTeleBot, types

with open(f'API/TOKEN.txt', 'r', encoding="utf-8") as f:
    TOKEN1 = f.read()
bot1 = AsyncTeleBot(TOKEN1)

async def runpingusers():
    directory = 'users'
    userslist = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    for ul in userslist:
        try:
            await bot1.send_message(ul, text="Я снова готов к работе!\nНапишите /start или просто спросите у бота что он умеет, чтобы получить FAQ")
        except Exception as e:
            exmes = str(e)
            if exmes.find("bot was blocked by the user")!=-1:
                shutil.rmtree(f'users/{ul}')
        await asyncio.sleep(1)
        
async def wera():
    task123 = await asyncio.create_task(runpingusers())

asyncio.run(wera())