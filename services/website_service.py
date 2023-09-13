import requests
import codecs
import os
import uuid

class WebsiteService():

    def create_new_post(self, title, text):  # публикация новой новости на сайте
        url = 'http://localhost:5000/admin'  # URL вебсайта (проект Website)

        #  заголовок новости берется из файла resources/website/title.txt
        img_save_path = os.path.join(
            os.getcwd(), os.path.join('web', 'static', 'img.jpg')
        )

        print(title)
        print(text)

        # --------------------------------  формирование запроса
        myobj = {
            'title': title,
            'text': text,
        }

        # Генерация уникального UUID
        random_uuid = uuid.uuid4()

        # Преобразование в строку и удаление дефисов
        random_file_name = str(random_uuid).replace('-', '')

        files = {'img': (f'{random_file_name}.jpg', open(img_save_path, 'rb'), 'image/jpeg')}

        x = requests.post(url, data=myobj, files=files)  # отправка запроса

        print(x.text)
