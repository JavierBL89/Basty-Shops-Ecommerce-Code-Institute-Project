# Generated by Django 3.2 on 2022-08-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20220816_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]