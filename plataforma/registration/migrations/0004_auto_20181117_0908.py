# Generated by Django 2.1.3 on 2018-11-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20181117_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='celphone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
