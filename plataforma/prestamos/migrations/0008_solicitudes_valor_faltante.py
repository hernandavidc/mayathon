# Generated by Django 2.1.3 on 2018-11-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0007_auto_20181117_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudes',
            name='valor_Faltante',
            field=models.IntegerField(default=0),
        ),
    ]
