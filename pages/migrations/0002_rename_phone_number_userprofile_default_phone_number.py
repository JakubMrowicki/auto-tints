# Generated by Django 3.2.8 on 2021-10-23 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number',
            new_name='default_phone_number',
        ),
    ]