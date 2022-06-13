# Generated by Django 4.0.5 on 2022-06-13 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_list', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=255)),
                ('votes', models.IntegerField(default=0)),
                ('grocery_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='grocery.list')),
            ],
        ),
    ]
