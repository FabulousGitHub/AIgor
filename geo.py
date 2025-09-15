# packages
import requests
import json
import time
from fake_useragent import UserAgent
import asyncio

# geocoder class
class Geocoder:
    # base url
    base_url = 'https://nominatim.openstreetmap.org/search'
    
    # results
    results = []

    def fetch(self, address):
        # headers
        ua = UserAgent()
        head = ua.random
        headers = {
            'User-Agent': f'{head}'
        }
        
        # string query parameters
        params = {
            'q': address,
            'format': 'geocodejson'
        }
        # make HTTP GET request to Nominatim API
        res = requests.get(url=self.base_url, params=params, headers=headers)
        #print('HTTP GET request to URL: %s | Status code: %s' % (res.url, res.status_code))
        if res.status_code == 200:
            return res
        else:
            return None
    
    def parse(self, res):
        try:
            label = json.dumps(res['features'][0]['properties']['geocoding']['label'], indent=2)
            coordinates = json.dumps(res['features'][0]['geometry']['coordinates'], indent=2).replace('\n', '').replace('[', '').replace(']', '').strip()                       
            # retrieved data
            self.results = ({
                'address': label,
                'coordinates': coordinates
            })
            
        except:
            return False
            pass
        
    async def run(self,address):
        task = self.fetch(address)
        if task==None:
            await asyncio.sleep(1)
            task = self.fetch(address)
            if task==None:
                return False
        try:
            res = task.json()
            if (self.parse(res))!=False:
                s = str(self.results)
                s = s[s.find('coordinates'):]
                s = s[s.find(':')+3:]
                longt = float(s[:s.find(',')])
                langt = float(s[s.find(',')+1:s.find("'")])
                return [langt,longt]
            else:
                return False
        except:
            return False
# main driver
async def getcoordinates(adr,tgid):
    newjsonpath = f'users/{tgid}/note.json'
    town = (adr.find("hometown")==-1)
    with open(newjsonpath, "r") as json_file:
        json_read = json_file.read()
    data = json.loads(json_read)
    hometown = str(data[0]["0"]["hometown"])
    if town==False:
        if data[0]["0"]["hometown"]!="":
            adr = adr.replace("hometown",str(data[0]["0"]["hometown"]))
            hometown = str(data[0]["0"]["hometown"])
        else:
            adr = adr.replace("hometown","")
            hometown = ""
    geocoder = Geocoder()
    task = await asyncio.create_task(geocoder.run(adr))
    if task!=False:
        task.append(hometown)
    return task

async def sethometown(town,tgid):
    try:
        newjsonpath = f'users/{tgid}/note.json'
        with open(newjsonpath, "r") as json_file:
            json_read = json_file.read()
        data = json.loads(json_read)
        data[0]["0"]["hometown"] = town
        with open(newjsonpath, "w", encoding='ascii') as json_file:
            json_file.write(json.dumps(data))
        return f'Город поиска установлен: {town}'
    except:
        return False
#asyncio.run(getcoordinates('Казань XL','1470047914'))
