from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
import requests

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(default='', verbose_name="Содержание")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def publish(self):
        if not self.is_published:
            self.published_date = timezone.now()
            self.is_published = True
            self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-published_date']
