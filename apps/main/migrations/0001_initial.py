# Generated by Django 4.1 on 2022-10-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteConfiguration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        default="logo.png",
                        help_text="Логотип сайта",
                        upload_to="Изображение",
                        verbose_name="Логотип",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="УК Новый город",
                        max_length=128,
                        verbose_name="Название",
                    ),
                ),
                (
                    "tagline",
                    models.CharField(
                        help_text="Работа найдется для каждого",
                        max_length=128,
                        verbose_name="Слоган",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        help_text="Москва", max_length=128, verbose_name="Город"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        help_text="ул.Свободы", max_length=256, verbose_name="Улица"
                    ),
                ),
                (
                    "num_building",
                    models.CharField(
                        help_text="д.5", max_length=5, verbose_name="Номер здания"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="Номер телефона в формате - 79823212334",
                        max_length=11,
                        null=True,
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="info@uk.ru", max_length=254, verbose_name="e-mail"
                    ),
                ),
                (
                    "site",
                    models.CharField(
                        help_text="www.uk-newcity.ru",
                        max_length=128,
                        verbose_name="Сайт",
                    ),
                ),
                (
                    "key_ya",
                    models.CharField(
                        blank=True,
                        help_text="1888f9f3-1174-48c4-b1b4-fa129bй2345234",
                        max_length=128,
                        verbose_name="Api-ключ Яндекса",
                    ),
                ),
                (
                    "lat",
                    models.CharField(
                        blank=True,
                        help_text="57.167979",
                        max_length=64,
                        verbose_name="Широта",
                    ),
                ),
                (
                    "lon",
                    models.CharField(
                        blank=True,
                        help_text="65.564430",
                        max_length=64,
                        verbose_name="Долгота",
                    ),
                ),
                (
                    "footer_copyright",
                    models.CharField(
                        blank=True,
                        default="Все права защищены © Москва 2021 - 2022 гг.",
                        max_length=256,
                        verbose_name="Футер копирайт",
                    ),
                ),
                (
                    "dev_info",
                    models.CharField(
                        default="Команда №4",
                        max_length=128,
                        verbose_name="Информация о разработчиках сайта",
                    ),
                ),
                (
                    "vk",
                    models.CharField(
                        default="https://vk.com/",
                        max_length=128,
                        verbose_name="Страница ВКонтакте",
                    ),
                ),
                (
                    "im",
                    models.CharField(
                        default="https://instagram.com/",
                        max_length=128,
                        verbose_name="Страница Instagram",
                    ),
                ),
                (
                    "fb",
                    models.CharField(
                        default="https://facebook.com/",
                        max_length=128,
                        verbose_name="Страница Facebook",
                    ),
                ),
                (
                    "tw",
                    models.CharField(
                        default="https://twitter.com/",
                        max_length=128,
                        verbose_name="Страница Twitter",
                    ),
                ),
            ],
            options={"verbose_name": "Настройки сайта",},
        ),
    ]
