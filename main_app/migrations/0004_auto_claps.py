# Generated by Django 2.2.5 on 2019-10-09 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='claps',
            field=models.IntegerField(default=0),
        ),
    ]
