# Generated by Django 3.2.13 on 2023-09-27 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategories',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
