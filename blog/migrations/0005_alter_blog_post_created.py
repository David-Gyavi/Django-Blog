# Generated by Django 3.2.6 on 2021-09-06 21:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_post_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 21, 18, 40, 445988, tzinfo=utc)),
        ),
    ]
