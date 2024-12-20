# Generated by Django 5.1.3 on 2024-12-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('FonoCliente', models.PositiveIntegerField()),
                ('gmail', models.CharField(max_length=50)),
                ('password_cliente', models.CharField(max_length=50)),
                ('FechaNacimiento', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
    ]
