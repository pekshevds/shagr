# Generated by Django 3.1.4 on 2021-01-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quant',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
    ]