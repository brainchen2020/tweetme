# Generated by Django 2.1.2 on 2018-10-30 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='parent',
        ),
    ]
