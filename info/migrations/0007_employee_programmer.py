# Generated by Django 4.2.17 on 2024-12-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_employee_livestatusby_employee_livestatusdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='programmer',
            field=models.BooleanField(default=0),
        ),
    ]