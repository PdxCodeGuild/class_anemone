# Generated by Django 4.0.5 on 2022-06-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField(max_length=250)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
