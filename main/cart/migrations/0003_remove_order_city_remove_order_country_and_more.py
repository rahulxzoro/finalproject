# Generated by Django 5.0.1 on 2024-02-02 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order_address_order_city_order_country_order_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pincode',
        ),
    ]