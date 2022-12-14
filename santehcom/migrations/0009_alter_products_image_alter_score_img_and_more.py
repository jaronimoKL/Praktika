# Generated by Django 4.1.1 on 2022-10-16 13:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santehcom', '0008_score_img_alter_products_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='score',
            name='img',
            field=models.FileField(upload_to='stars/%Y/%m/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])], verbose_name='Изображение кол-ва звёзд'),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(upload_to='avatar/%Y/%m/', verbose_name='Аватарка'),
        ),
    ]
