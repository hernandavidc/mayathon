# Generated by Django 2.1.3 on 2018-11-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0002_auto_20181117_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudes',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
