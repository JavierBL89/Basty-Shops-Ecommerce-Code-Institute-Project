# Generated by Django 3.2 on 2022-08-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20220816_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
