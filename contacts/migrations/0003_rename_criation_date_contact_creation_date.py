# Generated by Django 4.1.3 on 2022-11-19 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_date_criation_contact_criation_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='criation_date',
            new_name='creation_date',
        ),
    ]
