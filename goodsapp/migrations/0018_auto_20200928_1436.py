# Generated by Django 3.1.1 on 2020-09-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0017_auto_20200928_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='template',
            field=models.ManyToManyField(blank=True, to='goodsapp.PropertySetTemplate', verbose_name='Шаблон'),
        ),
    ]