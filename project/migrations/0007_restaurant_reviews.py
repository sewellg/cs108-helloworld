# Generated by Django 4.0.3 on 2022-04-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_menu_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='reviews',
            field=models.TextField(blank=True),
        ),
    ]
