# Generated by Django 3.1.7 on 2021-04-02 00:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0019_auto_20210401_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 17, 13, 44, 707146)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='commons.school'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 17, 13, 44, 706680)),
        ),
    ]
