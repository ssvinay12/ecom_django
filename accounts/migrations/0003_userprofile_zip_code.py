# Generated by Django 3.1 on 2022-03-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
