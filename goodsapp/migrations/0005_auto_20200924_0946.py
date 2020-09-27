# Generated by Django 2.2.4 on 2020-09-24 06:46

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0004_objectpropertyvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpropertyvalue',
            name='value',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='property', chained_model_field='property', on_delete=django.db.models.deletion.CASCADE, to='goodsapp.Value', verbose_name='Значение'),
        ),
    ]