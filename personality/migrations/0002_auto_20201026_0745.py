# Generated by Django 3.1.2 on 2020-10-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')], max_length=100),
        ),
    ]
