# Generated by Django 5.1.1 on 2024-10-05 23:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodateApp', '0015_productreview_delete_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('whatsapp', models.CharField(default=0, max_length=20)),
                ('phone', models.CharField(default=0, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=300)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
