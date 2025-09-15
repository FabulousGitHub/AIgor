from googlesearch import search
import codecs
import requests
import asyncio
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()
head = ua.random
headers = {
    'User-Agent': f'{head}' 
}

async def gsearch(rqst):
    head = ua.random
    headers = {
        'User-Agent': f'{head}' 
    }
    search0 = search(rqst,lang="ru",region="russia",sleep_interval=5,num_results=5)
    answer = "0"
    for url in search0:
        try:
            link = str(url)
            responce = requests.get(link, headers=headers)
            soup = BeautifulSoup(responce.text, "html.parser")
            x = soup.get_text("|")
            x.replace('\n','')
            if len(x)>1000:
                x = x[0:1000]
            answer=answer+x
        except:
            pass
    return answer
async def urldescribe(link):
    head = ua.random
    headers = {
        'User-Agent': f'{head}' 
    }
    answer = "0"
    responce = requests.get(link, headers=headers)
    await asyncio.sleep(1)
    soup = BeautifulSoup(responce.text, "html.parser")
    x = soup.get_text("|")
    x.replace('\n','')
    if len(x)>10000:
        x = x[0:10000]
    answer=x
    return answer
