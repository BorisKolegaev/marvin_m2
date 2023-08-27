import os
import openai
import requests


class OpenAiService:
    def __init__(self):
        #openai.api_key = os.environ["OPENAI_API_KEY"]
        openai.api_key = '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'
        self.messages = [
            {"role": "system", "content": "You are a kind helpful assistant."},
        ]
        self.posts = [
            {"role": "system", "content": "You are a kind helpful assistant."},
        ]
        self.img_number = 1
        self.img_size = '256x256'
        self.img_save_path = os.path.join(
            os.getcwd(), os.path.join('web', 'static', 'img.jpg')
        )

    def send_message(self, msg):
        self.messages.append(
            {"role": "user", "content": msg},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        reply = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        print(reply)
        return reply

    def generate_img(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=self.img_number,
            size=self.img_size
        )
        img_url = response['data'][0]['url']
        img = requests.get(img_url)
        if img.status_code == 200:
            with open(self.img_save_path, 'wb') as f:
                f.write(img.content)

    def generate_post(self, prompt):
        prompt += ". Сформируй новость для сайта на основе этой информации"
        self.posts.append(
            {"role": "user", "content": prompt},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.posts
        )
        reply = chat.choices[0].message.content
        self.posts.append({"role": "assistant", "content": reply})
        print(reply)
        return reply


if __name__ == "__main__":
    oas = OpenAiService()
    oas.generate_img("pig")
