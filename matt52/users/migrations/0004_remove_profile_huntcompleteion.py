# Generated by Django 3.1.5 on 2021-01-18 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210115_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='huntcompleteion',
        ),
    ]
