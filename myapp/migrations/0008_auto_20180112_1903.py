# Generated by Django 2.0 on 2018-01-12 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_problems_mydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]