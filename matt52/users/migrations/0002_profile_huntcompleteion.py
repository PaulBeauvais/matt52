# Generated by Django 3.1.5 on 2021-01-15 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='huntcompleteion',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 1, 18, 43, 989070)),
            preserve_default=False,
        ),
    ]
