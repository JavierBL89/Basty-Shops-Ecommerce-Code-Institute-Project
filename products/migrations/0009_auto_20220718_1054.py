# Generated by Django 3.2 on 2022-07-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sizes_list',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.BooleanField(default=True),
        ),
    ]
