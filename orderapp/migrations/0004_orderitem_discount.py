# Generated by Django 3.0.5 on 2020-12-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0003_auto_20201213_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Скидка, %'),
        ),
    ]
