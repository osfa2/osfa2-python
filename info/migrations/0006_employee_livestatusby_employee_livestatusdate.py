# Generated by Django 4.2.17 on 2024-12-11 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_employee_livestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='livestatusby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='employee_livestatusby', to='info.employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='livestatusdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]