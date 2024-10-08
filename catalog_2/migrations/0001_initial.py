# Generated by Django 5.1.1 on 2024-10-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название продукта', max_length=50, verbose_name='Название продукта')),
                ('number_version', models.IntegerField(help_text='Введите номер версии', verbose_name='Номер версии')),
                ('name_version', models.CharField(help_text='Введите название версии', max_length=100, verbose_name='Название версии')),
                ('photo', models.ImageField(blank=True, help_text='Загрузите фото для статьи', null=True, upload_to='articles_/photo', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания статьи в базе данных')),
                ('view_counter', models.PositiveIntegerField(default=0, help_text='Подсчёт просмотров', verbose_name='Счётчик просмотров')),
                ('is_active', models.BooleanField(default=True, help_text='Укажите текущая это версия или нет', verbose_name='Текущая версия')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', 'number_version', 'name_version'],
            },
        ),
    ]