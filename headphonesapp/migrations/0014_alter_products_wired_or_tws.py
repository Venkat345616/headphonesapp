# Generated by Django 5.0.1 on 2024-02-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headphonesapp', '0013_remove_myuser_cart_items_cartitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='wired_or_TWS',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]