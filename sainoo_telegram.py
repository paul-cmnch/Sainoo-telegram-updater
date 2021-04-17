import json
from telegram import Bot
from config import Bot_token


def send(dic):
    my_bot = Bot(token=Bot_token)
    message = f"<a href='{dic['logolink']}'> </a>" \
              f"<a href='{dic['''joblink''']}'>{dic['positiontitle']}</a>\n\n" \
              f"<b>Company:  </b>{dic['companyname']}\n" \
              f"<b>Location:  </b>{dic['postcode']}, {dic['city']}, {dic['country']}\n" \
              f"<b>Type:  </b>{dic['postingtype']}\n\n" \
              f"<b>Deadline:  </b>{dic['deadline']}"

    print(message)
    with open('/home/paul/Python_projects/sainoo_active_users.json', 'r') as f:
        active_users = json.load(f)
    for i in active_users:
        my_bot.send_message(chat_id=i, text=message, parse_mode='HTML')
