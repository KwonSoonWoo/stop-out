# Generated by Django 2.0.6 on 2018-06-14 08:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 14, 8, 23, 39, 427396, tzinfo=utc)),
        ),
    ]
