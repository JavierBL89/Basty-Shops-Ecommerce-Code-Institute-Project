# Generated by Django 3.2 on 2022-07-17 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220717_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
