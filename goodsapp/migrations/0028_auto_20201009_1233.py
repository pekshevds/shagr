# Generated by Django 3.1.2 on 2020-10-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0027_auto_20201008_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='uid_1c',
            field=models.SlugField(blank=True, max_length=36, null=True, verbose_name='Идентификатор в 1С'),
        ),
    ]
