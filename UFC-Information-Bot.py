from API_Sportradar import *
import requests
import tok
# import json

token = tok.token
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0

# https://api.telegram.org/bot662911899:AAFrQda-GbuS3jvwFL5jli7K8LLbdWqaNIM/sendmessage?chat_id=783958880&text=hi


def get_updates():
    url = URL + 'getupdates'
    response = requests.get(url)
    return response.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {
            'chat_id': chat_id,
            'text': message_text
        }
        return message
    return None


def send_message(chat_id, text="Wait"):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def send_photo(chat_id, photo):
    url = URL + 'sendPhoto?chat_id={}&photo={}'.format(chat_id, photo)
    requests.get(url)


def main():
    # d = get_updates()
    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)
    while True:
        answer = get_message()
        try:
            if answer != None:
                chat_id = answer['chat_id']
                text = answer['text']

                if text == '/start':
                    send_message(chat_id, doc)
                elif text == '/top':
                    send_message(chat_id, rankings())
                elif '/fnum' in text and (len(text) == 6 or len(text) == 7) and (int(text[5]) >= 1 and int(text[5]) <= 10):
                    send_message(chat_id, about_f(int(text[5:])))
                elif text == '/coming':
                    send_message(chat_id, coming())
                elif text == '/champion':
                    send_photo(chat_id, 'http://www.mmaplanet.nl/wp-content/uploads/2018/04/Khabib.jpg')

            else:
                continue
        except ValueError:
            pass


if __name__ == '__main__':
    main()
