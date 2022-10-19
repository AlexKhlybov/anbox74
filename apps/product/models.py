import os
from uuid import uuid4

from django.db import models
from django.utils import timezone

from apps.main.mixins.utils import ActiveMixin, CreateUpdateMixin
from django.core.validators import MaxValueValidator, MinValueValidator 


def upload_to_news(instance, filename):
    if instance.pk:
        try:
            product = Product.objects.filter(pk=instance.pk).first()
            if product and product.image:
                product.image.delete()
        except (OSError, FileNotFoundError) as _:
            pass
    ext = filename.split('.')[-1]
    return os.path.join('product', f'{uuid4()}.{ext}')


class ProductCategory(ActiveMixin):
    name = models.CharField(verbose_name="Название", max_length=32)

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"

    def __str__(self):
        return self.name


class Manufacturer(ActiveMixin):
    name = models.CharField(verbose_name="Производитель", max_length=32)

    class Meta:
        verbose_name = "Название производителя"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.name


class City(CreateUpdateMixin):
    city = models.CharField(verbose_name="Страна", max_length=32)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.city


class Product(ActiveMixin):
    # TODO Подумать над default==1
    category = models.ForeignKey(ProductCategory, verbose_name="Категория", related_name="category", on_delete=models.CASCADE, default=1)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="Производитель", related_name="manufacturer", on_delete=models.CASCADE, default=1)
    
    article = models.CharField(verbose_name="Артикул", max_length=256)
    title = models.CharField(verbose_name="Название товара", max_length=256)
    sub_title = models.CharField(verbose_name="Подгазоловок", null=True, blank=True, max_length=256)
    image = models.FileField(max_length=64, verbose_name='Картинка', upload_to=upload_to_news)
    
    short_text = models.CharField(max_length=255, verbose_name='Короткое описание')
    text = models.TextField(max_length=10000, verbose_name='Описание продукта')
    
    city = models.ForeignKey(City, verbose_name="Страна", on_delete=models.CASCADE, default=1)
    price = models.DecimalField(verbose_name="Цена", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="Кол-во", default=0)
    sale = models.IntegerField(verbose_name="Скидка, %", validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    
    class Meta:
        abstract = True
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.title} ({self.article})"

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True)


class Boiler(Product):
    # TODO Вынести в базовый класс под наследование
    power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Номинальная мощность, кВт')
    voltage = models.CharField(max_length=255, null=True, blank=True, verbose_name='Номинальное напряжение, В')
    step_power = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ступень переключения, кВт')
    protect_class = models.CharField(max_length=255, null=True, blank=True, verbose_name='Класс защиты поражения током')
    temp_out = models.CharField(max_length=255, null=True, blank=True, verbose_name='Регулировка темп. на выходе, С')
    square = models.CharField(max_length=255, null=True, blank=True, verbose_name='Площадь отапливаемых помещений, м2')
    without_measure = models.CharField(max_length=255, null=True, blank=True, verbose_name='Габаритные размеры, мм (без патрубков)')
    with_measure = models.CharField(max_length=255, null=True, blank=True, verbose_name='Габаритные размеры, мм (c патрубков)')
    mass = models.CharField(max_length=255, null=True, blank=True, verbose_name='Масса, кг')
    heater_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='Тип нагревателя')
    max_pressure = models.CharField(max_length=255, null=True, blank=True, verbose_name='Максимальное давление в системе, Bar')
    pipe = models.CharField(max_length=255, null=True, blank=True, verbose_name='Диаметр трубы, дюйм')
    coolant = models.CharField(max_length=255, null=True, blank=True, verbose_name='Теплоноситель')
    
    
    class Meta:
        verbose_name = "Котел"
        verbose_name_plural = "Котлы"
