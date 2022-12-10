import os
from uuid import uuid4

from django.db import models
from solo.models import SingletonModel


def upload_to_delivery(instance, filename):
    if instance.pk:
        try:
            news = Delivery.objects.filter(pk=instance.pk).first()
            if news and news.image:
                news.image.delete()
        except (OSError, FileNotFoundError) as _:
            pass
    ext = filename.split('.')[-1]
    return os.path.join('delivery', f'{uuid4()}.{ext}')

class SiteConfiguration(SingletonModel):
    logo = models.ImageField(
        verbose_name="Логотип",
        upload_to="Изображение",
        default="logo.png",
        help_text="Логотип сайта",
    )
    name = models.CharField(verbose_name="Название", max_length=128, help_text="AnBox", default="AnBox")
    tagline = models.CharField(verbose_name="Слоган", max_length=128, help_text="Тепло с доставкой в каждый дом", default="Тепло с доставкой в каждый дом")
    city = models.CharField(verbose_name="Город", max_length=128, help_text="Миасс", default="Миасс")
    street = models.CharField(verbose_name="Улица", max_length=256, help_text="Свободы")
    num_building = models.CharField(verbose_name="Номер здания", max_length=5, help_text="1", default="1")
    phone = models.CharField(
        verbose_name="Телефон", max_length=11, null=True, blank=True, help_text="Номер телефона в формате - 79823212334", default="78888888888"
    )
    email = models.EmailField(verbose_name="e-mail", help_text="info@uk.ru", default="info@anbox74.ru")
    site = models.CharField(verbose_name="Сайт", max_length=128, help_text="www.anbox74.ru", default="www.anbox74.ru")

    key_ya = models.CharField(
        verbose_name="Api-ключ Яндекса", max_length=128, blank=True, help_text="1888f9f3-1174-48c4-b1b4-fa129bй2345234"
    )
    lat = models.CharField(verbose_name="Широта", max_length=64, blank=True, help_text="57.167979")
    lon = models.CharField(verbose_name="Долгота", max_length=64, blank=True, help_text="65.564430")

    footer_copyright = models.CharField(
        max_length=256, blank=True, default="Все права защищены © Миасс 2021 - 2022 гг.", verbose_name="Футер копирайт"
    )
    
    vk = models.CharField(max_length=128, default="https://vk.com/", verbose_name="Страница ВКонтакте")
    im = models.CharField(max_length=128, default="https://instagram.com/", verbose_name="Страница Instagram")
    fb = models.CharField(max_length=128, default="https://facebook.com/", verbose_name="Страница Facebook")
    tw = models.CharField(max_length=128, default="https://twitter.com/", verbose_name="Страница Twitter")


    def get_absolute_url(self):
        return f"/media/{self.logo}"

    def __str__(self):
        return "Настройки сайта"

    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
    
    def get_site(self):
        return f'{self.site}'

    class Meta:
        verbose_name = "Настройки сайта"


class Delivery(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    title = models.CharField(max_length=128, verbose_name='Название')
    image = models.FileField(max_length=64, verbose_name='Картинка', upload_to=upload_to_delivery)
    url = models.CharField(max_length=120, blank=True, verbose_name='Ссылка')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Компания доставки'
        verbose_name_plural = 'Компании доставки'

    def __str__(self):
        return self.title
