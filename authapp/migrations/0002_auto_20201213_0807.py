# Generated by Django 3.0.5 on 2020-12-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
    ]
