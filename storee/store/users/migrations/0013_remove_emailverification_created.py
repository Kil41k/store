# Generated by Django 3.2.13 on 2023-09-30 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_emailverification_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailverification',
            name='created',
        ),
    ]
