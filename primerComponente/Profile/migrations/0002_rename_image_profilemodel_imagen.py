# Generated by Django 4.0.1 on 2022-03-08 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='image',
            new_name='imagen',
        ),
    ]
