# Generated by Django 2.0.6 on 2019-02-21 18:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cwApp', '0002_auto_20190221_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publishDate',
            field=models.DateField(default=datetime.datetime(2019, 2, 21, 18, 4, 17, 80560, tzinfo=utc)),
        ),
    ]
