# Generated by Django 2.2.7 on 2019-11-20 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten_url', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturlmodel',
            name='count',
        ),
    ]
