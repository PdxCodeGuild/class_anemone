# Generated by Django 4.0.6 on 2022-07-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('cohort', models.CharField(max_length=50)),
                ('favorite_topic', models.CharField(max_length=100)),
                ('favorite_teacher', models.CharField(max_length=100)),
                ('capstone', models.URLField()),
                ('create_date_time', models.DateTimeField(auto_now_add=True)),
                ('update_date_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-create_date_time'],
            },
        ),
    ]
