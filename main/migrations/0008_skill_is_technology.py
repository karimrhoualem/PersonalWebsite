# Generated by Django 3.2.8 on 2021-10-31 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_skill_is_framework'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_technology',
            field=models.BooleanField(default=False),
        ),
    ]