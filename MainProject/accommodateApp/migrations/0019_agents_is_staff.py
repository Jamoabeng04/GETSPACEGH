# Generated by Django 5.1.1 on 2024-10-05 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodateApp', '0018_agents_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='agents',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
