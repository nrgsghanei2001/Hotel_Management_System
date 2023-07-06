# Generated by Django 3.2.9 on 2023-07-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='availability',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
