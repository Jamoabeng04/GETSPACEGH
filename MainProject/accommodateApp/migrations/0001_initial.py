# Generated by Django 5.1.1 on 2024-09-05 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('whatsapp', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accommodateApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('rate', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('vicinity', models.CharField(max_length=100)),
                ('rooms', models.TextField()),
                ('amenities', models.TextField()),
                ('images', models.ImageField(upload_to='uploads/products/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accommodateApp.category')),
                ('manager', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accommodateApp.manager')),
            ],
        ),
    ]
