# Generated by Django 4.0.5 on 2022-07-16 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-first_name']},
        ),
    ]
