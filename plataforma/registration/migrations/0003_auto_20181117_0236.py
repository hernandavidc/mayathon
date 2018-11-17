# Generated by Django 2.1.3 on 2018-11-17 07:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0004_auto_20181117_0236'),
        ('registration', '0002_auto_20180717_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='celphone',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='ranking',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='prestamos.Rankings'),
            preserve_default=False,
        ),
    ]