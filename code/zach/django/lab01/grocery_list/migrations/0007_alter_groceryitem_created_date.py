# Generated by Django 4.0.5 on 2022-07-06 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0006_alter_groceryitem_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
