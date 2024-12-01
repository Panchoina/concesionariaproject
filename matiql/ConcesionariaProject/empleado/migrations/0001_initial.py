# Generated by Django 3.1.12 on 2024-12-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('FonoEmpleado', models.PositiveIntegerField()),
                ('gmail', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=16)),
                ('FechaNacimiento', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'Empleado',
            },
        ),
    ]
