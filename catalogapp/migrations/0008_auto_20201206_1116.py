# Generated by Django 3.1.3 on 2020-12-06 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0007_auto_20201206_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='author',
        ),
    ]