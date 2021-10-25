# Generated by Django 3.2.8 on 2021-10-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]
