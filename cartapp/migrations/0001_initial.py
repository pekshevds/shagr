# Generated by Django 3.1.4 on 2020-12-09 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogapp', '0008_auto_20201206_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзина',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant', models.DecimalField(decimal_places=3, default=1, max_digits=15, verbose_name='Количество')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapp.cart', verbose_name='Корзина')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogapp.good', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Элементы корзины',
                'verbose_name_plural': 'Элемент корзины',
            },
        ),
    ]
