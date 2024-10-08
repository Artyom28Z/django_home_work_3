# Generated by Django 5.1.1 on 2024-10-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "catalog_2",
            "0006_alter_product_options_remove_product_number_version_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.CharField(
                blank=True,
                help_text="Введите описание продукта",
                max_length=250,
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото продукта",
                null=True,
                upload_to="catalog_2/photo",
                verbose_name="Фото",
            ),
        ),
    ]
