# Generated by Django 4.0.3 on 2022-03-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_address',
            field=models.TextField(blank=True),
        ),
    ]
