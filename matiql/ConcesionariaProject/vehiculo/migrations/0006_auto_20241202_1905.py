# Generated by Django 3.1.12 on 2024-12-02 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0005_auto_20241202_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='descripcion',
            field=models.TextField(max_length=300),
        ),
    ]
