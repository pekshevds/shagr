# Generated by Django 3.0.4 on 2020-10-08 08:42

from django.db import migrations, models
import django.db.models.deletion
import goodsapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0025_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Наименование')),
                ('picture', models.ImageField(blank=True, default=None, null=True, upload_to=goodsapp.models.get_image_name, verbose_name='Изображение 200х200')),
                ('slug', models.SlugField(blank=True, max_length=36, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.AddField(
            model_name='good',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='goodsapp.Brand', verbose_name='Бренд'),
        ),
    ]
