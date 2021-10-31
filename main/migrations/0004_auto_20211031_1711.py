# Generated by Django 3.2.8 on 2021-10-31 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='certificate'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
