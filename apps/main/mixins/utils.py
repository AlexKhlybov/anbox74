from django.db import models


class CreateUpdateMixin(models.Model):
    """Примешивает поля даты создания и обновления"""

    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        abstract = True


class ActiveMixin(CreateUpdateMixin):
    """Примешивает поле актив, поля создания и обновления"""

    is_active = models.BooleanField(verbose_name="Включено", db_index=True, default=True)

    class Meta:
        abstract = True

    def delete(self):
        self.is_active = False
        self.save()
