# Generated by Django 4.0.5 on 2022-06-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_item', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField()),
                ('date_complete', models.DateTimeField(blank=True, null=True)),
                ('created_complete', models.BooleanField()),
            ],
        ),
    ]
