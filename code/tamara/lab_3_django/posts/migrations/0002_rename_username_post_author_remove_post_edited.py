# Generated by Django 4.0.5 on 2022-07-06 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='edited',
        ),
    ]
