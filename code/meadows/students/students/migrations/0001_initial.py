# Generated by Django 4.0.6 on 2022-07-18 20:47

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
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('cohort', models.CharField(max_length=300)),
                ('favorite_topic', models.CharField(max_length=300)),
                ('favorite_teacher', models.CharField(max_length=300)),
                ('captsone', models.CharField(max_length=100)),
            ],
        ),
    ]
