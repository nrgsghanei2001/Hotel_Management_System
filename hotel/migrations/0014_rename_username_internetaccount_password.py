# Generated by Django 4.2.3 on 2023-07-12 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_internetaccount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internetaccount',
            old_name='username',
            new_name='password',
        ),
    ]