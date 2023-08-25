import os
import webbrowser
import subprocess

import time
from services.open_ai_service import OpenAiService


class ExpertSystemService:

    def __init__(self):  # создание необходимых сервисов
        self.oas = OpenAiService()

    def osrun(self, cmd):  # метод для запуска программ в операционной системе
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

    def openurl(self, url):  # метод для открытия страниц в браузере
        webbrowser.open(url)

    def work(self, text):  # метод для обработки команд
        if "отмена" in text:
            return '1'
        elif ("открой" in text) or ("перейди" in text):
            if ("калькулятор" in text) or ("посчитай" in text):
                self.osrun('calc')
                return '2'
            elif ("paint" in text) or ("пэинт" in text):
                self.osrun('mspaint')
                return '3'
            elif ("youtube" in text) or ("ютуб" in text):
                self.openurl('http://youtube.com')
                return '4'
            elif ("сайт" in text) and ("центра" in text):
                self.openurl('https://www.untehdon.ru/')
                return '5'
        elif ("найди" in text) or ("найти" in text):
            if ("youtube" in text) or ("ютуб" in text) or ("ютюб" in text):
                text = text.replace('найди', '')
                text = text.replace('ютуб', '')
                text = text.replace('ютюб', '')
                text = text.replace('в интернете', '')
                text = text.strip()
                self.openurl('https://www.youtube.com/results?search_query=' + text)
                return '6'
            text = text.replace('найди', '')
            text = text.replace('ютуб', '')
            text = text.replace('в интернете', '')
            text = text.strip()
            self.openurl('https://www.google.com/search?q=' + text)
            return '7'

        # elif "создай" in text:
        #     dir_name = self.sp_to_txt.speech_to_text("ADD_DIR")
        #     os.mkdir(conf.DOCUMENTS_DIR + "/" + dir_name)
        #     return
        #
        # elif ("добавь" in text) or ("новость" in text):
        #     website = website_service()
        #     website.create_new_post()
        #
        # elif ("файл" in text) or ("перенеси" in text):
        #     list_of_files = glob.glob(conf.DOWNLOADS_DIR + "/*")
        #     latest_file = max(list_of_files, key=os.path.getctime)
        #     print(latest_file)
        #
        #     latest_file_updated = latest_file.replace("//", "\\")
        #     os.rename(latest_file_updated, latest_file_updated.replace(" ", "_"))
        #     print(latest_file_updated)
        #     os.popen("move " + latest_file_updated.replace(" ", "_") + " " + conf.DOCUMENTS_DIR)
        #     return

        elif "выход" in text:
            #raise SystemExit
            return 'error'


        else:  # В том случае если команда не найдена, отправить ее к GPT-3 боту и произнести ответ
            reply = self.oas.send_message(text)
            return reply
