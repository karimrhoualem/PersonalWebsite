# Generated by Django 3.2.8 on 2021-11-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_skill_is_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
