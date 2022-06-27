# Generated by Django 4.0.5 on 2022-06-23 23:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('short_url', '0004_remove_shorturl_id_alter_shorturl_small_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
