# Generated by Django 4.0.5 on 2022-06-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_rename_user_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='uname',
            field=models.CharField(default='username_here', max_length=200),
        ),
    ]
