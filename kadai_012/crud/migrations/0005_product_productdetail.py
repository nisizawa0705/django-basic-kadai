# Generated by Django 4.2.14 on 2024-08-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productDetail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
