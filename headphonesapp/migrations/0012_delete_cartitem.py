# Generated by Django 5.0.1 on 2024-01-31 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('headphonesapp', '0011_remove_myuser_quantity_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
