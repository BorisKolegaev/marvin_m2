import eel
from resources.config import PAGE_NAVIGATION
from services.chat_gpt_service import send_msg_to_gpt

# Set the web folder and start page
eel.init('web')


@eel.expose  # Expose this function to be called from the frontend
def my_python_function(parameter):
    # Your Python logic here
    return "Result from Python: " + parameter


@eel.expose
def load_page(page):
    with open(PAGE_NAVIGATION[page], 'r') as file:
        return file.read()


@eel.expose
def send_msg(msg):
    reply = send_msg_to_gpt(msg)
    return reply


eel.start('index.html', size=(800, 800))  # Start the app
