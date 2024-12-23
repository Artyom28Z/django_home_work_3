# Generated by Django 4.2.2 on 2024-10-29 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog_2", "0008_product_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        help_text="Введите название категории",
                        max_length=50,
                        verbose_name="Название категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name"],
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(
                default=False,
                help_text="Опубликовать или нет?",
                verbose_name="Публикация",
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="product",
                to="catalog_2.product",
                verbose_name="Продукт",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите категорию",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="category",
                to="catalog_2.category",
                verbose_name="Категория",
            ),
        ),
    ]
