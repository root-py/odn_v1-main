# Generated by Django 3.2.7 on 2021-09-10 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buoys', '0008_auto_20210909_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buoy',
            old_name='buoyname',
            new_name='model_number',
        ),
        migrations.AddField(
            model_name='buoy',
            name='measurement_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
