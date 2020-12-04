# Generated by Django 3.1.3 on 2020-11-27 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Фамилия')),
                ('phone', models.CharField(blank=True, max_length=150, null=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=1024, verbose_name='Адрес')),
                ('email', models.CharField(blank=True, max_length=30, verbose_name='Email')),
                ('locality', models.CharField(blank=True, default='', max_length=20, verbose_name='Нас. пункт')),
                ('street', models.CharField(blank=True, default='', max_length=30, verbose_name='Улица')),
                ('house', models.CharField(blank=True, default='', max_length=10, verbose_name='Дом')),
                ('apartments', models.CharField(blank=True, default='', max_length=10, verbose_name='Кв.')),
                ('porch', models.CharField(blank=True, default='', max_length=10, verbose_name='Подъезд')),
                ('floor', models.CharField(blank=True, default='', max_length=10, verbose_name='Этаж')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
    ]