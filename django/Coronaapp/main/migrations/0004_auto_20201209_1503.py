# Generated by Django 3.1.4 on 2020-12-09 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201209_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsentry',
            old_name='id',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='kunden',
            old_name='id',
            new_name='kunden_id',
        ),
    ]