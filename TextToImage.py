from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import asyncio

with open(f'API/GoogleDevAPI.txt', 'r', encoding="utf-8") as f:
    get_api_key = f.read()
client = genai.Client(api_key=get_api_key)

async def GenerateImage(request,tgid):

    contents = "Generate image. Prompt is "+request

    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=contents,
        config=types.GenerateContentConfig(
          response_modalities=['TEXT', 'IMAGE']
        )
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            continue
        elif part.inline_data is not None:
            image = Image.open(BytesIO((part.inline_data.data)))
            image.save(f'users/{tgid}/img.png')
            return True
        else:
            return False

async def EditImage(request,image,tgid):
    image = PIL.Image.open('/path/to/image.png')

    text_input = ('Hi, This is a picture of me.'
                'Can you add a llama next to me?',)

    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=[text_input, image],
        config=types.GenerateContentConfig(
          response_modalities=['TEXT', 'IMAGE']
        )
    )

    for part in response.candidates[0].content.parts:
      if part.text is not None:
        print(part.text)
      elif part.inline_data is not None:
        image = Image.open(BytesIO((part.inline_data.data)))
        image.show()

async def getgenimg(request,tgid):
    task = asyncio.create_task(GenerateImage(request,tgid))
    await task
    return str(task.result())

# asyncio.run(getgenimg("Fast car","1470047914"))