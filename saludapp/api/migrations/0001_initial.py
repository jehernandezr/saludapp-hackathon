# Generated by Django 3.0.8 on 2020-08-01 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cedula', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('fechaNacimiento', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('cedula', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('fechaNacimiento', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Disponible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('tipo', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('C', 'Cancelada'), ('R', 'Reservada'), ('L', 'Libre'), ('F', 'Finalizada')], default='L', max_length=250)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=250)),
                ('fechaCreada', models.DateField(auto_now_add=True)),
                ('disponible', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Disponible')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Paciente')),
            ],
        ),
    ]
