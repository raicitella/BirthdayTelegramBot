import telebot
from datetime import datetime
from datetime import date
import time
import threading
import os
from dotenv import load_dotenv
from datetime import datetime
from zoneinfo import ZoneInfo
from telebot import util
from telebot import types

load_dotenv()

API_TOKEN=os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

Group_chat_id = None
THREAD_ID = None

TZ=ZoneInfo("Europe/Moscow")

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):   
    chat_id = message.chat.id
    username= message.from_user.username
    bot.reply_to(message, f"""\
Привет, @{username}! \
""")

@bot.message_handler(commands=['time'])
def send_time(message):   
    chat_id = message.chat.id
    now = datetime.now(TZ)    
    Startbot = bot.reply_to(message, now)

@bot.message_handler(commands=['birthdays'])
def send_welcome(message):   
    chat_id = message.chat.id
    text1 = """
#🎂 Дни рождения

##Январь

Имя                     | Дата
------------------------|----------------
user4      | 1 января

##Апрель

Имя                     | Дата
------------------------|----------------
user1             | 5 апреля

##Май

Имя                     | Дата
------------------------|----------------
user3         | 13 мая
user5         | 13 мая

##Июнь

Имя                     | Дата
------------------------|----------------
user2    | 22 июня   

"""
    if chat_id == Group_chat_id:
        bot.send_rich_message(
                    chat_id=message.chat.id,
                    rich_message=types.InputRichMessage(markdown=text1),
                    message_thread_id=message.message_thread_id
            )
    else:
        bot.send_rich_message(
                        chat_id=message.chat.id,
                        rich_message=types.InputRichMessage(markdown=text1),
                )

        
@bot.message_handler(commands=['check'])
def send_welcome(message):
    now = datetime.now(TZ)
    current_date = now.date()
    dr = []
    i = 0

    while i<len(birthdays):
        if (current_date == birthdays[i].replace(year=current_date.year)):
            dr.append(birthdays[i])
            i+=1
        else:
            i+=1
    q = 0
    if len(dr)>0:
        while q < len(dr):
            bot.reply_to(
                message,
                text=f"🎉 Сегодня {birthdaysName[dr[q]]} отмечает свой день рождения!" 
            )
            q+=1
    else:
        bot.reply_to(
                message,
                text=f"Сегодня никто не отмечает свой день рождения!"
            )
    
birthdays = [
date(2000, 4, 5),
date(2000, 6, 22),
date(2000, 5, 13),
date(2000, 1, 1),
date(2001, 5, 13),]

birthdaysName = {

date(2000, 4, 5):"user1",
date(2000, 6, 22):"user2",
date(2000, 5, 13):"user3",
date(2000, 1, 1):"user4",
date(2001, 5, 13):"user5"
}

def happyBirthday():
    now = datetime.now(TZ)
    current_date = now.date()
    dr = []
    i = 0

    while i<len(birthdays):
        if (current_date == birthdays[i].replace(year=current_date.year)):
            dr.append(birthdays[i])
            i+=1
        else:
            i+=1
    q = 0
    if len(dr)>0:
        while q < len(dr):
            bot.send_message(
                chat_id=chat_id,
                text=f"🎉 Сегодня {birthdaysName[dr[q]]} отмечает свой день рождения!",  message_thread_id=THREAD_ID 
            )
            q+=1

last_date = None

def run():
    global last_date
    while True:
        now = datetime.now(TZ)
        today=now.date()
        if last_date != today:
            happyBirthday()
            last_date = today
        time.sleep(60)
threading.Thread(target=run, daemon=True).start()

bot.infinity_polling()