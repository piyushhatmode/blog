# Generated by Django 2.0.2 on 2018-05-04 07:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 7, 46, 36, 446651, tzinfo=utc)),
        ),
    ]
