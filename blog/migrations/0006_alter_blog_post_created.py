# Generated by Django 3.2.6 on 2021-09-06 21:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_post_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 21, 19, 53, 62711, tzinfo=utc)),
        ),
    ]
