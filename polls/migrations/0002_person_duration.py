# Generated by Django 4.0.3 on 2022-03-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
