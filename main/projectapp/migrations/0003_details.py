# Generated by Django 5.0.1 on 2024-01-29 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_alter_category_options_category_slug_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('pincode', models.IntegerField()),
                ('city', models.TextField()),
                ('country', models.TextField()),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
