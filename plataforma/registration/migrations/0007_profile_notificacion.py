# Generated by Django 2.1.3 on 2018-11-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20181117_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='notificacion',
            field=models.BooleanField(default=False),
        ),
    ]
