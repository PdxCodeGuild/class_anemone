# Generated by Django 4.0.5 on 2022-06-17 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
