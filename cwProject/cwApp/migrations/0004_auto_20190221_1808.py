# Generated by Django 2.0.6 on 2019-02-21 18:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cwApp', '0003_auto_20190221_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pageNumber',
            new_name='page',
        ),
        migrations.AlterField(
            model_name='book',
            name='publishDate',
            field=models.DateField(default=datetime.datetime(2019, 2, 21, 18, 8, 48, 555319, tzinfo=utc)),
        ),
    ]