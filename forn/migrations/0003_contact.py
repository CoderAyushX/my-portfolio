# Generated by Django 4.0 on 2022-01-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forn', '0002_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
