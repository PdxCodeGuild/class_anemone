# Generated by Django 4.0.5 on 2022-06-16 17:12

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
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField()),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('complete', models.BooleanField()),
            ],
        ),
    ]
