import requests
from django.conf import settings

TELEGRAM_BOT_TOKEN = settings.BOT_TOKEN
TELEGRAM_CHANNEL_ID = settings.CHAT_ID

def send_telegram_message(post):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    text = f"📝 *{post.title}*\n\n{post.content}"  
    params = {
        'chat_id': TELEGRAM_CHANNEL_ID,
        'text': text,
        'parse_mode': 'Markdown',
    }
    try:
        response = requests.post(url, data=params)
        if response.status_code != 200:
            print(f"Ошибка отправки в Telegram: {response.json()}")
    except Exception as e:
        print(f"Произошла ошибка при отправке в Telegram: {e}")