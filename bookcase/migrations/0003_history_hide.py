# Generated by Django 3.0.8 on 2021-10-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcase', '0002_auto_20211027_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]
