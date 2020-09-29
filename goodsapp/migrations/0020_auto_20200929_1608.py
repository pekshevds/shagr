# Generated by Django 2.2.4 on 2020-09-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0019_auto_20200928_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='is_service',
            field=models.BooleanField(default=False, verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='good',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='Спецпредложение'),
        ),
        migrations.AlterField(
            model_name='good',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='Новинка'),
        ),
        migrations.AlterField(
            model_name='good',
            name='is_sale',
            field=models.BooleanField(default=False, verbose_name='Распродажа'),
        ),
    ]
