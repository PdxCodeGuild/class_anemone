# Generated by Django 4.0.6 on 2022-08-15 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0002_groceryitem_complete_groceryitem_completed_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
