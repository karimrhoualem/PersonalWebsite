# Generated by Django 3.2.8 on 2021-10-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211031_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_framework',
            field=models.BooleanField(default=False),
        ),
    ]
