# Generated by Django 5.1.1 on 2024-10-09 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog_2", "0005_alter_product_number_version"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="number_version",
        ),
        migrations.AddField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="product",
                to="catalog_2.product",
                verbose_name="продукт",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото для статьи",
                null=True,
                upload_to="catalog_2/photo",
                verbose_name="Фото",
            ),
        ),
    ]
