# Generated by Django 3.2.8 on 2021-11-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_portfolio_image_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image_filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
