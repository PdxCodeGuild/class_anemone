# Generated by Django 4.0.5 on 2022-06-23 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Member',
        ),
    ]
