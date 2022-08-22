# Generated by Django 4.0.5 on 2022-06-14 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(verbose_name='created date')),
                ('completed_date', models.DateTimeField(verbose_name='completed date')),
            ],
        ),
    ]
