# Generated by Django 3.1.7 on 2021-04-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_user',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
