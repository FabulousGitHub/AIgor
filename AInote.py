import ujson as json
import os
import asyncio
import shutil

async def savenote(s,tgid):
    newjsonpath = f'users/{tgid}/note.json'
    try:
        s=s[s.find("{"):s.find("}")+1]
        note = json.loads(s)
        with open(newjsonpath, "r") as json_file:
            json_read = json_file.read()
        data = json.loads(json_read)
        i = 1
        while(i<=5 and data[i][str(i)]["title"]!=""):
            i+=1
        
        if i<6:
            data[i][str(i)]["title"] = note["title"]
            data[i][str(i)]["main"] = note["main"]
            data[i][str(i)]["place"] = note["place"]
            data[i][str(i)]["time"] = note["time"]
            data[i][str(i)]["timetoping"] = note["timetoping"]
            data[i][str(i)]["pingnote"] = note["pingnote"]
            data[i][str(i)]["ainote"] = note["ainote"]
            with open(newjsonpath, "w", encoding='ascii') as json_file:
                json_file.write(json.dumps(data))
            return (f'Заметка №{i} создана')
        else:
            return ("Лимит записей 5, удалите ненужные заметки")
    except:
        return ("Не удалось создать заметку")

async def createuser(tgid):
    newpath = f'users/{tgid}'
    newjsonpath = f'users/{tgid}/note.json'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        if not os.path.exists(newjsonpath):
            shutil.copy2('examples/note.json',newjsonpath)
    else:
        return True

async def deleteusernote(num,tgid):
    try:
        newjsonpath = f'users/{tgid}/note.json'
        if os.path.exists(newjsonpath):
            with open(newjsonpath, "r") as json_file:
                json_read = json_file.read()
            data = json.loads(json_read)
            if data[num][str(num)]["time"]!="":
                data[num][str(num)]["title"] = ""
                data[num][str(num)]["main"] = ""
                data[num][str(num)]["place"] = ""
                data[num][str(num)]["time"] = ""
                data[num][str(num)]["timetoping"] = ""
                data[num][str(num)]["pingnote"] = ""
                data[num][str(num)]["ainote"] = ""
                with open(newjsonpath, "w", encoding='ascii') as json_file:
                    json_file.write(json.dumps(data))
                return (f'Заметка №{num} удалена')
            else:
                return (f'Заметки №{num} не существует')
        else:
            return (f'Пользователь {tgid} не зарегистрирован')
    except:
        return "Не получилось удалить заметку, ошибка сервера..."

async def clearusernotelist(tgid):
    try:
        newjsonpath = f'users/{tgid}/note.json'
        with open(newjsonpath, "r") as json_file:
            json_read = json_file.read()
        data = json.loads(json_read)
        for num in range(1,6):
            data[num][str(num)]["title"] = ""
            data[num][str(num)]["main"] = ""
            data[num][str(num)]["place"] = ""
            data[num][str(num)]["time"] = ""
            data[num][str(num)]["timetoping"] = ""
            data[num][str(num)]["pingnote"] = ""
            data[num][str(num)]["ainote"] = ""
        with open(newjsonpath, "w", encoding='ascii') as json_file:
            json_file.write(json.dumps(data))
        return ('Список заметок очищен')
    except:
        return "Не удалось очистить, ошибка сервера..."

async def usernotelist(tgid):
    try:
        newjsonpath = f'users/{tgid}/note.json'
        with open(newjsonpath, "r") as json_file:
            json_read = json_file.read()
        data = json.loads(json_read)
        nt = ""
        for i in range(1,6):
            if data[i][str(i)]["title"]!="":
                nt0 = str(data[i][str(i)]["ainote"])
                nt = nt+f'\n№{i}.{nt0}\n'
        if nt=="":
            return False
        else:
            return nt
    except:
        return "Не удалось посмотреть, ошибка сервера..."
#asyncio.run(usernotelist("1470047914"))
