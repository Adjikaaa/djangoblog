from django.template.loader import render_to_string
from django.conf import settings
import urllib.request
import json



def get_html_message_from_template(post) -> str:
    return render_to_string('post_telegram_message.html', {
        'post': post
    })

def send_telegram_message(chat_id: str, post):
    api_url = f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage'

    input_data = json.dumps(
        {
            'chat_id': chat_id,
            'text': get_html_message_from_template(post=post),
            'parse_mode': "HTML"
        }
    ).encode()

    try:
        req = urllib.request.Request(
            url=api_url,
            data=input_data,
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))

    except Exception as e:
        print(e)