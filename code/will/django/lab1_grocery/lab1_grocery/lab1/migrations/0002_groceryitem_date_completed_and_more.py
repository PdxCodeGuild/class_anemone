# Generated by Django 4.0.5 on 2022-06-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date completed'),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='task_completed',
            field=models.BooleanField(),
        ),
    ]
