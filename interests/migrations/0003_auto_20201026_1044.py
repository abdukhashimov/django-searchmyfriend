# Generated by Django 3.1.2 on 2020-10-26 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0002_auto_20201026_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interest',
            old_name='userId',
            new_name='user',
        ),
    ]