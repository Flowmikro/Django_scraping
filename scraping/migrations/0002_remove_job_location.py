# Generated by Django 4.2.4 on 2023-08-10 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
    ]
