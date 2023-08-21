import os
import openai


openai.api_key = os.environ["OPENAI_API_KEY"]

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]


def send_msg_to_gpt(msg):
    global messages
    messages.append(
        {"role": "user", "content": msg},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(reply)
    return reply

