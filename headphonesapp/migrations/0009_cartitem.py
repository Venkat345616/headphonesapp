# Generated by Django 5.0.1 on 2024-01-31 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headphonesapp', '0008_myuser_cart_items_alter_products_accessories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='headphonesapp.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='headphonesapp.myuser')),
            ],
        ),
    ]
