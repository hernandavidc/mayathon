# Generated by Django 2.1.3 on 2018-11-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudes',
            name='fecha_solicitud',
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='estado',
            field=models.CharField(choices=[('a', 'Aceptado'), ('r', 'Rechazado'), ('p', 'Proceso')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Estados',
        ),
    ]
