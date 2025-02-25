from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from .telegram_utils import send_telegram_message

@receiver(post_save, sender=Post)
def post_save_handler(sender, instance, **kwargs):
    if instance.is_published and not getattr(instance, '_telegram_sent', False):
        # Отправляем пост в Telegram только если он опубликован
        send_telegram_message(instance)
        instance._telegram_sent = True 