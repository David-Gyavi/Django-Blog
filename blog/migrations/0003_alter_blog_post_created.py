# Generated by Django 3.2.6 on 2021-08-25 22:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210823_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 25, 22, 3, 11, 592563, tzinfo=utc)),
        ),
    ]