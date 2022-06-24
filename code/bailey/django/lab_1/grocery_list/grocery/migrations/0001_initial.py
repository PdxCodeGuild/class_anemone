# Generated by Django 4.0.5 on 2022-06-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groceryitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
