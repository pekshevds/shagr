# Generated by Django 5.2.1 on 2025-06-05 10:12

import catalog_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0009_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='good',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=catalog_app.models.get_image_name1, verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='good',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=catalog_app.models.get_image_name1, verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='good',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=catalog_app.models.get_image_name2, verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='good',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=catalog_app.models.get_image_name3, verbose_name='Изображение 3'),
        ),
        migrations.AlterField(
            model_name='good',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=catalog_app.models.get_image_name4, verbose_name='Изображение 4'),
        ),
    ]
