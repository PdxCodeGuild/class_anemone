# Generated by Django 4.0.5 on 2022-06-13 22:45

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
                ('description', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(verbose_name='created')),
                ('date_completed', models.DateTimeField(verbose_name='completed')),
                ('is_done', models.BooleanField(verbose_name='is complete')),
            ],
        ),
    ]
