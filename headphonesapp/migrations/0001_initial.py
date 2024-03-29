# Generated by Django 5.0.1 on 2024-01-30 13:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('launch', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('image1', models.ImageField(upload_to='uploads/products/')),
                ('image2', models.ImageField(upload_to='uploads/products/')),
                ('image3', models.ImageField(upload_to='uploads/products/')),
                ('image4', models.ImageField(upload_to='uploads/products/')),
                ('image5', models.ImageField(upload_to='uploads/products/')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('offer', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=225)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
