# Generated by Django 4.0.6 on 2022-07-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerylist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
