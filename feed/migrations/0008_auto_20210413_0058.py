# Generated by Django 3.1.7 on 2021-04-12 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_add_feed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_feed',
            old_name='caption',
            new_name='name',
        ),
    ]
