import requests

TELEGRAM_BOT_TOKEN = '7777528511:AAHXKBZ80B0GXfwFAaH0H_L4sKV_8j-PuHs'
TELEGRAM_CHANNEL_ID = '@fregg007'

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