# Generated by Django 3.1.1 on 2020-10-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0024_category_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=36, verbose_name='Url'),
        ),
    ]
