# Generated by Django 4.2.17 on 2024-12-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_link_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='approved_usb',
            field=models.BooleanField(default=0),
        ),
    ]
