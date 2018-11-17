# Generated by Django 2.1.3 on 2018-11-17 07:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0003_auto_20181117_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadosInversiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NivelesDeRiesgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limiteInferior', models.IntegerField()),
                ('limiteSuperior', models.IntegerField()),
                ('riesgo', models.CharField(max_length=10)),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.AlterField(
            model_name='inversionistassolicitudes',
            name='estado',
            field=models.CharField(choices=[('s', 'Solicitado'), ('a', 'Aceptado'), ('r', 'Rechazado'), ('t', 'Inversión retornada'), ('z', 'Inversión realizada'), ('m', 'Inversión en mora')], max_length=1),
        ),
        migrations.AddField(
            model_name='solicitudes',
            name='nivelDeRiesgo',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.PROTECT, to='prestamos.NivelesDeRiesgo'),
            preserve_default=False,
        ),
    ]
