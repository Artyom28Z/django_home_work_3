from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Version(models.Model):
    product = models.ForeignKey(
        "Product",
        related_name="product",
        on_delete=models.SET_NULL,
        verbose_name="Продукт",
        **NULLABLE
    )
    number_version = models.FloatField(
        verbose_name="Номер версии", help_text="Введите номер версии", unique=True
    )
    name_version = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    is_active = models.BooleanField(
        verbose_name="Текущая версия",
        help_text="Укажите текущая это версия или нет",
        default=True,
    )

    def __str__(self):
        return f"{self.number_version}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["number_version", "name_version"]


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.CharField(
        max_length=250, verbose_name="Описание", help_text="Введите описание продукта",
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to="catalog_2/photo",
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
        **NULLABLE
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания продукта в базе данных"
    )
    view_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров", help_text="Подсчёт просмотров", default=0
    )
    user_product = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    is_active = models.BooleanField(
        verbose_name="Публикация",
        help_text="Опубликовать или нет?",
        default=False,
    )
    category = models.ForeignKey(
        "Category",
        related_name="category",
        on_delete=models.SET_NULL,
        help_text="Укажите категорию",
        verbose_name="Категория",
        **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
        permissions = [("can_edit_description", "Can edit description"),
                       ("can_edit_category", "Can edit category"),
                       ("can_edit_is_active", "Can edit is_active")
                       ]
