# Generated by Django 3.1.4 on 2020-12-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_eventsentry_kunden_kundenevents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsentry',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kunden',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
