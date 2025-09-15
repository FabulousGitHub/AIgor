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

async def turnof():
    directory = 'users'
    userslist = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    for ul in userslist:
        await asyncio.sleep(1)
        try:
            await bot1.send_message(ul, text="Бот выключен, находится на update")
        except:
            pass
        
async def wera():
    task123 = await asyncio.create_task(turnof())

asyncio.run(wera())