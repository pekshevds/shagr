# Generated by Django 3.0.5 on 2020-12-07 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlistapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Записи', 'verbose_name_plural': 'Избранное'},
        ),
    ]