from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField('Ссылка', max_length=255, blank=True, null=True)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    logged_in_only = models.BooleanField('Только для авторизованных', default=False)
    guest_only = models.BooleanField('Только для гостей', default=False)

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
