# Generated by Django 3.2.13 on 2023-09-16 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('descriptoin', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('descriptoin', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('img', models.ImageField(upload_to='ProductsImages')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcategories')),
            ],
        ),
    ]
