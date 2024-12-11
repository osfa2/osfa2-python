# Generated by Django 4.2.17 on 2024-12-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_department_livestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='livestatus',
            field=models.IntegerField(blank=True, choices=[(1, 'Offline'), (2, 'Working from Home'), (3, 'At Desk'), (4, 'Available'), (5, 'Away From Desk'), (6, 'Lobby'), (7, 'In Meeting')], default=1),
        ),
    ]