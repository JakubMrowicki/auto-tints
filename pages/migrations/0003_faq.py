# Generated by Django 3.2.8 on 2021-10-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_phone_number_userprofile_default_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collapse_id', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
            ],
        ),
    ]
