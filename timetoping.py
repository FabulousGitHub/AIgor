import datetime as dt
import time
import ujson as json
import asyncio
import shutil
import os
import AInote
from telebot.async_telebot import AsyncTeleBot, types

with open(f'API/TOKEN.txt', 'r', encoding="utf-8") as f:
    TOKEN1 = f.read()
bot1 = AsyncTeleBot(TOKEN1)
warning_text = f'Сообщения можно присылать раз в 15 сек из-за ограничений Telegram API\nСледующее сообщение можно прислать через '
async def lastmessagetime(tgid):
    newjsonpath = f'users/{tgid}/note.json'
    qpath = f'users/queue.json'
#     try:
    with open(qpath, "r") as json_fileq:
        json_readq = json_fileq.read()
    dataq = json.loads(json_readq)
    while int(dataq[0]["15count"])>15:
        with open(qpath, "r") as json_fileq:
            json_readq = json_fileq.read()
        dataq = json.loads(json_readq)
        await bot1.send_message(tgid,text='Ваш запрос в очереди, подождите')
        await asyncio.sleep(16)
    dataq[0]["15count"]=str(int(dataq[0]["15count"])+1)
    dataq[0]["requests"]=str(int(dataq[0]["requests"])+1)
    with open(qpath, "w") as json_fileq:
        json_fileq.write(json.dumps(dataq))
    ########################################
    with open(newjsonpath, "r") as json_file:
        json_read = json_file.read()
    data = json.loads(json_read)
    new = int(data[0]["0"]["new"])
    new = new+1
    data[0]["0"]["new"]=str(new)
    if new<100:
        if int(data[0]["0"]["banscore"])<16:
            if str(data[0]["0"]["lstmsg"])=="":
                data[0]["0"]["lstmsg"] = str(dt.datetime.now()+dt.timedelta(hours=3))[:-7]
                with open(newjsonpath, "w") as json_file:
                    json.dump(data, json_file)
                return True
            else:
                time_last = dt.datetime.strptime(str(data[0]["0"]["lstmsg"]), "%Y-%m-%d %H:%M:%S")
                time_now = dt.datetime.now()+dt.timedelta(hours=3)
                if int(data[0]["0"]["banscore"])<5:
                    if dt.timedelta(seconds=15)<time_now - time_last:
                        data[0]["0"]["lstmsg"] = (dt.datetime.now()+dt.timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
                        data[0]["0"]["banscore"] = "0"
                        with open(newjsonpath, "w") as json_file:
                            json.dump(data, json_file)
                        return True
                    else:
                        data[0]["0"]["banscore"] = str(int(data[0]["0"]["banscore"])+1) 
                        with open(newjsonpath, "w", encoding='ascii') as json_file:
                            json.dump(data, json_file)
                        return warning_text + str(dt.timedelta(seconds=15) - (time_now - time_last))[:-7]
                else:
                    if dt.timedelta(seconds=15)<time_now - time_last:
                        data[0]["0"]["banscore"] = "0"
                        with open(newjsonpath, "w") as json_file:
                            json.dump(data, json_file)
                        return True
                    else:
                        data[0]["0"]["banscore"] = str(int(data[0]["0"]["banscore"])+1)
                        with open(newjsonpath, "w") as json_file:
                            json.dump(data, json_file)
                        return f'Подозрение на спам! Вы tgid:{tgid} можете быть забанены'
        else:
            return 'Вы были забанены за спам!'
    else:
        return 'Вы исчерпали дневной лимит 100 запросов. Счетчик запросов обновится в 00:00!'
#     except:
#         return 'Повторите запрос, сервер не смог обработать'

async def pingusers():
    delay = 60
    directory = 'users'
    while 1 > 0:
        userslist = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
        #print(userslist)
        for ul in userslist:
            #print(ul)
            try:
                with open(f'users/{ul}/note.json', "r") as json_file:
                    json_read = json_file.read()
                data = json.loads(json_read)
                time_now = dt.datetime.now()+dt.timedelta(hours=3)
                time_now = str(time_now)[:-7]
                time_now = dt.datetime.strptime(time_now,'%Y-%m-%d %H:%M:%S')
                for i in range(1,6):
                    if data[i][str(i)]["timetoping"]!="":
                        ttp = str(data[i][str(i)]["timetoping"])
                        ttp = dt.datetime.strptime(ttp,'%Y-%m-%d %H:%M:%S')
                        if time_now>ttp:
                            await bot1.send_message(ul, text='Напоминаю:\n'+data[i][str(i)]["pingnote"])
                            data[i][str(i)]["timetoping"]=""
                            with open(f'users/{ul}/note.json', "w") as json_file:
                                json.dump(data, json_file)
                    elif data[i][str(i)]["time"]!="":
                        ttpdelnote = str(data[i][str(i)]["time"])
                        ttpdelnote = dt.datetime.strptime(ttpdelnote,'%Y-%m-%d %H:%M:%S')
                        if time_now>ttpdelnote:
                            t = await AInote.deleteusernote(i,ul)
                            await bot1.send_message(ul, text=f'{t} (вышло время события)\nТекст заметки:\n'+data[i][str(i)]["ainote"])
            except:
                continue
        #print("pingusers")
        await asyncio.sleep(delay)

async def countupdate():
    delay = 15
    qpath = f'users/queue.json'
    while 1 > 0:
        time_now = str(dt.datetime.now())
        time_now = time_now[11]+time_now[12]
        with open(qpath, "r") as json_fileq:
            json_readq = json_fileq.read()
        dataq = json.loads(json_readq)
        if dataq[0]["15count"]!="0":
            dataq[0]["15count"] = 0
            with open(qpath, "w") as json_fileq:
                json_fileq.write(json.dumps(dataq))
        if time_now=="00":
            dataq[0]["requests"]=0
            with open(qpath, "w") as json_fileq:
                json_fileq.write(json.dumps(dataq))
        await asyncio.sleep(delay)

async def requestsupdate():
    delay = 1800
    qpath = f'users/queue.json'
    directory = 'users'
    while 1 > 0:
        time_now = str(dt.datetime.now())
        time_now = time_now[11]+time_now[12]
        with open(qpath, "r") as json_fileq:
            json_readq = json_fileq.read()
        dataq = json.loads(json_readq)
        commoncount = str(dataq[0]["requests"])
        if time_now=="22":
            await bot1.send_message("1470047914", text="Запросов сегодня: "+commoncount)
            dataq[0]["requests"]=0
            with open(qpath, "w") as json_fileq:
                json_fileq.write(json.dumps(dataq))
            userslist = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
            for ul in userslist:
                try:
                    with open(f'users/{ul}/note.json', "r") as json_file:
                        json_read = json_file.read()
                    data = json.loads(json_read)
                    data[0]["0"]["new"] = "0"
                    with open(f'users/{ul}/note.json', "w") as json_file:
                        json_file.write(json.dumps(data))
                except:
                    continue
        await asyncio.sleep(delay)


# async def wera():
#     task123 = await asyncio.create_task(runpingusers())
#     print(task123)

# asyncio.run(wera())