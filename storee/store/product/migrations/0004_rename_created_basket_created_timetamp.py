# Generated by Django 3.2.13 on 2023-09-30 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20230927_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='created',
            new_name='created_timetamp',
        ),
    ]
