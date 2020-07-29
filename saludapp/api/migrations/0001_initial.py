# Generated by Django 2.1.3 on 2020-07-27 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=250)),
                ('fechaCita', models.DateTimeField()),
                ('fechaCreada', models.DateField(auto_now_add=True)),
                ('tipoCita', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('cedula', models.AutoField(primary_key=True, serialize=False)),
                ('fechaNacimiento', models.DateField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('cedula', models.AutoField(primary_key=True, serialize=False)),
                ('fechaNacimiento', models.DateField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Medico'),
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]