# Birthday Telegram Bot

Этот Telegram-бот предназначен для поздравления участников группы с днём рождения.  
Он работает на Python и проверяет каждый день, кто отмечает день рождения, чтобы отправить поздравление в указанный чат.

---

## Функции

- /start — приветствие пользователя.  
- /birthdays — выводит список всех участников и их даты рождения.  
- /check — проверяет, кто празднует день рождения сегодня и отправляет сообщение.  
- Автоматическая проверка каждый день и отправка поздравлений в чат.

---
## Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone https://github.com/RaicitellaDeveloper/BirthdayTelegramBot.git
cd birthday-bot
```
2. Установите зависимости:
```bash
pip install pyTelegramBotAPI python-dotenv
```
3. Создайте файл .env и добавте токен:
```bash
BOT_TOKEN=ВАШ_ТОКЕН
```
4. Измените в коде значения:
```bash
chat_id - на ID вашего чата
#если используются темы (topics)
THREAD_ID - на ID ветки,куда бот отправляет сообщения
```
ЕСЛИ ТЕМЫ В ЧАТЕ НЕ ИСПОЛЬЗУЮТСЯ ТО В СТРОКАХ:
```python
bot.send_message(
            chat_id=chat_id,
            text=f"🎉 Сегодня {birthdaysName[dr[q]]} отмечает свой день рождения!",  message_thread_id=THREAD_ID 
        )
```
УБЕРИТЕ:
```python 
message_thread_id=THREAD_ID
```
5. Запустите бота:
```bash
python main.py