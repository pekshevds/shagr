# Generated by Django 3.1.1 on 2020-09-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0016_auto_20200925_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.ManyToManyField(blank=True, to='goodsapp.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='property',
            name='template',
            field=models.ManyToManyField(to='goodsapp.PropertySetTemplate', verbose_name='Шаблон'),
        ),
    ]