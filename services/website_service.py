import requests
import codecs


class WebsiteService():

    def create_new_post(self, title, text):  # публикация новой новости на сайте
        url = 'http://localhost:5000/admin'  # URL вебсайта (проект Website)

        #  заголовок новости берется из файла resources/website/title.txt

        print(title)
        print(text)

        # --------------------------------  формирование запроса
        myobj = {
            'title': title,
            'text': text
        }

        x = requests.post(url, data=myobj)  # отправка запроса

        print(x.text)
