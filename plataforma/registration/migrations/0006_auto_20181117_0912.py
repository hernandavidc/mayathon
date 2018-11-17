# Generated by Django 2.1.3 on 2018-11-17 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20181117_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ranking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='prestamos.Rankings'),
        ),
    ]
