# Generated by Django 5.2.1 on 2025-05-31 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_catalog_seo_description_catalog_seo_keywords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='items', to='catalog_app.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 3'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение 4'),
        ),
    ]
