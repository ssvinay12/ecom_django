# Generated by Django 3.1 on 2022-03-07 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='coming_soon',
        ),
    ]
