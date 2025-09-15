import datetime as dt
import time
import json
import asyncio
import os
import AInote
from telebot.async_telebot import AsyncTeleBot, types

TOKEN1 = ''
TestTOKEN1 = ''
bot1 = AsyncTeleBot(TestTOKEN1)
time_mindelta = dt.datetime.strptime("00:00:15",'%H:%M:%S')-dt.datetime.strptime("00:00:00",'%H:%M:%S')
warning_text = f'Сообщения можно присылать раз в 15 сек из-за ограничений Telegram API\nСледующее сообщение можно прислать через '
async def lastmessagetime(tgid):
    newjsonpath = f'users/{tgid}/note.json'
    qpath = f'users/queue.json'
    try:
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
        with open(qpath, "w", encoding='ascii') as json_fileq:
            json_fileq.write(json.dumps(dataq))
        ########################################
        with open(newjsonpath, "r") as json_file:
            json_read = json_file.read()
        data = json.loads(json_read)
        if int(data[0]["0"]["banscore"])<16:
            if data[0]["0"]["lstmsg"]=="":
                data[0]["0"]["lstmsg"] = dt.datetime.now().strftime('%y-%m-%d %H:%M:%S')
                with open(newjsonpath, "w", encoding='ascii') as json_file:
                    json_file.write(json.dumps(data))
                return True
            else:
                time_last = dt.datetime.strptime(data[0]["0"]["lstmsg"],'%y-%m-%d %H:%M:%S')
                time_now = dt.datetime.now().strftime('%y-%m-%d %H:%M:%S')
                time_now = dt.datetime.strptime(time_now,"%y-%m-%d %H:%M:%S")
                time_delta = time_now - time_last
                if int(data[0]["0"]["banscore"])<5:
                    if time_mindelta<time_delta:
                        data[0]["0"]["lstmsg"] = dt.datetime.now().strftime('%y-%m-%d %H:%M:%S')
                        data[0]["0"]["banscore"] = str(0)
                        with open(newjsonpath, "w", encoding='ascii') as json_file:
                            json_file.write(json.dumps(data))
                        return True
                    else:
                        data[0]["0"]["banscore"] = str(int(data[0]["0"]["banscore"])+1) 
                        with open(newjsonpath, "w", encoding='ascii') as json_file:
                            json_file.write(json.dumps(data))
                        return warning_text + str(time_mindelta - time_delta)
                else:
                    if time_mindelta<time_delta:
                        data[0]["0"]["banscore"] = "0"
                        with open(newjsonpath, "w", encoding='ascii') as json_file:
                            json_file.write(json.dumps(data))
                        return True
                    else:
                        data[0]["0"]["banscore"] = str(int(data[0]["0"]["banscore"])+1)
                        with open(newjsonpath, "w", encoding='ascii') as json_file:
                            json_file.write(json.dumps(data))
                        return f'Подозрение на спам! Вы tgid:{tgid} можете быть забанены'
        else:
            return 'Вы были забанены за спам!'
    except:
        return 'Повторите запрос, сервер не смог обработать'

async def pingusers():
    delay = 30
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
                time_now = dt.datetime.now().strftime('%H:%M')
                time_now = dt.datetime.strptime(time_now,'%H:%M')
                for i in range(1,6):
                    if data[i][str(i)]["timetoping"]!="":
                        ttp = str(data[i][str(i)]["timetoping"])
                        ttp = dt.datetime.strptime(ttp,'%H:%M')
                        if time_now>ttp:
                            await bot1.send_message(ul, text='Напоминаю:\n'+data[i][str(i)]["pingnote"])
                            data[i][str(i)]["timetoping"]=""
                            with open(f'users/{ul}/note.json', "w", encoding='ascii') as json_file:
                                json_file.write(json.dumps(data))
                    elif data[i][str(i)]["time"]!="":
                        ttpdelnote = str(data[i][str(i)]["time"])
                        ttpdelnote = dt.datetime.strptime(ttpdelnote,'%H:%M')
                        if time_now>ttpdelnote:
                            t = await AInote.deleteusernote(i,ul)
                            await bot1.send_message(ul, text=f'{t} (вышло время события)\nТекст заметки:\n'+data[i][str(i)]["ainote"])
            except:
                continue
        print("pingusers")
        await asyncio.sleep(delay)

async def countupdate():
    delay = 15
    qpath = f'users/queue.json'
    while 1 > 0:
        with open(qpath, "r") as json_fileq:
            json_readq = json_fileq.read()
        dataq = json.loads(json_readq)
        if dataq[0]["15count"]!="0":
            dataq[0]["15count"] = 0
            with open(qpath, "w", encoding='ascii') as json_fileq:
                json_fileq.write(json.dumps(dataq))
        await asyncio.sleep(delay)

async def turnof():
    directory = 'users'
    userslist = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    for ul in userslist:
        await bot1.send_message(ul, text="Бот выключен, находится на update")

async def runpingusers():
    directory = 'users'
    userslist = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    for ul in userslist:
        await bot1.send_message(ul, text="Я снова готов к работе!")
        #await bot1.send_message(ul, text="Меня включили, я готов к работе\nКрайние добавленные функции:\n1.Оповещение о включении/выключении бота\n2.Теперь бот может описать,что на изображении.Просто отправьте фото в диалог.")