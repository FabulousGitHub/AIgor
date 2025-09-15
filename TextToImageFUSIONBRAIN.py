import json
import asyncio
import requests
import base64

class FusionBrainAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key ',
            'X-Secret': f'Secret ',
        }

    def get_pipeline(self):
        response = requests.get(self.URL + 'key/api/v1/pipelines', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, pipeline, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f'{prompt}'
            }
        }
        data = {
            'pipeline_id': (None, pipeline),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/pipeline/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    async def check_generation(self, name, request_id, attempts=30, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/pipeline/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                images = data['result']['files']
                # Здесь image_base64 - это строка с данными изображения в формате base64
                image_base64 = images[0]
                # Декодируем строку base64 в бинарные данные
                image_data = base64.b64decode(image_base64)
                # Открываем файл для записи бинарных данных изображения
                with open(f"users/{name}/img.jpg", "wb") as file:
                    file.write(image_data)
                attempts = 1
            attempts -= 1
            await asyncio.sleep(delay)


async def getgenimg(text,name):
    api = FusionBrainAPI('https://api-key.fusionbrain.ai/', '', '')
    pipeline_id = api.get_pipeline()
    uuid = api.generate(text, pipeline_id)
    task = asyncio.create_task(api.check_generation(name,uuid))
    await task
#asyncio.run(getgenimg("Компьютер игровой","1470047914"))