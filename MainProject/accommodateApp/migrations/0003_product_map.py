# Generated by Django 5.1.1 on 2024-09-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodateApp', '0002_pricerange_product_condition_product_rules_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='map',
            field=models.URLField(default=0, max_length=500, null=True),
        ),
    ]
