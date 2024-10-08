from django.db import models

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название продукта", help_text="Введите название продукта"
    )
    number_version = models.FloatField(verbose_name="Номер версии", help_text="Введите номер версии", unique=True)
    name_version = models.CharField(max_length=100, verbose_name="Название версии", help_text="Введите название версии")
    photo = models.ImageField(
        upload_to="articles_/photo",
        verbose_name="Фото",
        help_text="Загрузите фото для статьи",
        **NULLABLE
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания статьи в базе данных"
    )

    view_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров", help_text="Подсчёт просмотров", default=0
    )
    is_active = models.BooleanField(
        verbose_name="Текущая версия",
        help_text="Укажите текущая это версия или нет",
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "number_version", "name_version"]