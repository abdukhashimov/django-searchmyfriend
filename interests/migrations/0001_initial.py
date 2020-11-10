# Generated by Django 3.1.2 on 2020-11-10 13:57

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), size=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='user.user')),
            ],
        ),
    ]
