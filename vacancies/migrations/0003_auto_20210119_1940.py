# Generated by Django 3.1.5 on 2021-01-19 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_auto_20210119_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='speciality',
            new_name='specialty',
        ),
    ]
