# Generated by Django 4.1 on 2022-08-08 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
