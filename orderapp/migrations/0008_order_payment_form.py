# Generated by Django 3.1.2 on 2021-11-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0007_auto_20210104_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_form',
            field=models.CharField(choices=[('AW', 'Онлайн'), ('BN', 'Безналичные'), ('ON', 'Наличные')], default='NL', max_length=2, verbose_name='Форма оплаты'),
        ),
    ]
