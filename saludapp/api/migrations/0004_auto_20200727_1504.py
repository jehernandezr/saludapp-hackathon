# Generated by Django 3.0.7 on 2020-07-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200727_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='fechaNacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fechaNacimiento',
            field=models.DateField(),
        ),
    ]
