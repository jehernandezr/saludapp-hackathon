# Generated by Django 3.0.8 on 2020-07-28 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_child_userlogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 15, 2, 42, 928557)),
        ),
    ]
