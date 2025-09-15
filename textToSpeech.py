import asyncio
from edge_tts import Communicate

async def text_to_speech(text, sex, tgid):
    try:
        v = "ru-RU-DmitryNeural"
        if sex==0:
            v = "ru-RU-SvetlanaNeural"
        communicate = Communicate(text, voice=v)  # Change the voice as needed
        output_file = f'users/{tgid}/tts.mp3'
        await communicate.save(output_file)
        return output_file
    except:
        return False