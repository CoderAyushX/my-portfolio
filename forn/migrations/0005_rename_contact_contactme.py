# Generated by Django 4.0 on 2022-01-05 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forn', '0004_rename_email_contact_gmail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contactMe',
        ),
    ]
