# Generated by Django 3.1.7 on 2021-04-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0006_auto_20210416_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]