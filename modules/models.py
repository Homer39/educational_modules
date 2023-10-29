from django.db import models


class Module(models.Model):
    "Модель описывающая модули"
    number = models.IntegerField(verbose_name='Порядковый номер')
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return f"Модуль {self.name}"

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"