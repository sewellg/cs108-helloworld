# Generated by Django 4.0.3 on 2022-04-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_remove_restaurant_rescuisine_restaurant_rescuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]