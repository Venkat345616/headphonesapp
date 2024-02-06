# Generated by Django 5.0.1 on 2024-01-31 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headphonesapp', '0007_products_accessories_products_wired_or_tws'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='cart_items',
            field=models.ManyToManyField(blank=True, to='headphonesapp.products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='accessories',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='brand_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/'),
        ),
    ]
