import eel
import threading
from resources.config import PAGE_NAVIGATION
from services.open_ai_service import OpenAiService
from services.voice_control_service import VoiceControlService
from services.expert_system_service import ExpertSystemService
from services.website_service import WebsiteService


eel.init('web')

voice_thread = threading.Event()


@eel.expose
def load_page(page):
    with open(PAGE_NAVIGATION[page], 'r', encoding='UTF-8') as file:
        return file.read()


@eel.expose
def send_message(msg):
    ess = ExpertSystemService()
    reply = ess.work(msg)
    return reply


@eel.expose
def start_voice_control():
    global voice_thread
    voice_thread = threading.Thread(target=VoiceControlService().start_voice_control)
    voice_thread.start()


@eel.expose
def stop_voice_control():
    pass


@eel.expose
def gen_image(prompt):
    oas = OpenAiService()
    oas.generate_img(prompt)


@eel.expose
def gen_txt(prompt):
    oas = OpenAiService()
    response = oas.generate_post(prompt)
    return response


@eel.expose
def create_post(generated_text, title):
    web = WebsiteService()
    web.create_new_post(title, generated_text)

eel.start('index.html', size=(800, 800))
