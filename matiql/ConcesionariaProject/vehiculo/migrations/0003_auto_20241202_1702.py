# Generated by Django 3.1.12 on 2024-12-02 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('vehiculo', '0002_auto_20241202_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='dueño',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente_rut', to='cliente.cliente'),
        ),
    ]