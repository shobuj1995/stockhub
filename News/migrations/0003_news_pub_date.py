# Generated by Django 2.1.5 on 2019-02-06 18:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_sportnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 6, 18, 44, 52, 530011, tzinfo=utc)),
        ),
    ]
