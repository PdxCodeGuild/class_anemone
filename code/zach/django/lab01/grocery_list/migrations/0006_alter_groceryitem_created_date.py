# Generated by Django 4.0.5 on 2022-07-06 12:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0005_alter_groceryitem_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 6, 12, 58, 27, 363333, tzinfo=utc)),
        ),
    ]
