# Generated by Django 3.2 on 2022-02-03 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220203_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]