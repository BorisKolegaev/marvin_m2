import os
import requests
import json
import base64
import time
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat


class OpenAiService:
    def __init__(self):
        self.chat = GigaChat(
            credentials='ODI3YzQ1ZmMtMTdhNS00ODM2LTkyODQtjI2MTQ1Z2OmZmMmYwYjM4LTc1ZDMtNGU1MC05YmM1LTI5NzFkNWY0ZDg1OQ==', # сюда  key от GigaChat (Client или Secret не помню. Тот который длинее вроде)
            verify_ssl_certs=False)

        self.messages = [
            SystemMessage(
                content="Ты виртуальный ассисстент, тебя зовут Марвин"
            )
        ]

        self.posts = [
            SystemMessage(
                content="Ты создатель новостных текстов"
            )
        ]

        self.URL = 'https://api-key.fusionbrain.ai/'
        self.AUTH_HEADERS = {
            'X-Key': f'Key 82BA75D4CCFED5FCBC31390B08670AC',  # сюда api key от fusion brain
            'X-Secret': f'Secret B2BA54122E8F1C3698E00703C6871',  # сюда secret key от fusion brain
        }

        self.img_save_path = os.path.join(
            os.getcwd(), os.path.join('web', 'static', 'img.jpg')
        )

        self.model_id = self.get_model()

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def send_message(self, msg):
        self.messages.append(HumanMessage(content=msg))
        res = self.chat(self.messages)
        self.messages.append(res)
        return res.content

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def generate_img(self, prompt):
        uuid = self.generate(prompt, self.model_id)
        images = self.check_generation(uuid)[0]

        decoded_img_data = base64.b64decode(images)

        with open(self.img_save_path, "wb") as fh:
            fh.write(decoded_img_data)

    def generate_post(self, prompt):
        prompt += ". Сформируй новость для сайта на основе этой информации"
        self.posts.append(HumanMessage(content=prompt))
        res = self.chat(self.posts)
        self.posts.append(res)
        return res.content

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)


if __name__ == "__main__":
    oas = OpenAiService()
    print(oas.generate_img("собака победила в соревнованиях"))
