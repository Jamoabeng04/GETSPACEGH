# Generated by Django 5.1.1 on 2024-10-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodateApp', '0019_agents_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agents',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='agents',
            name='lastname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
