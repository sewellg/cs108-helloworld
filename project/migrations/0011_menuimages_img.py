# Generated by Django 4.0.3 on 2022-04-27 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_remove_restaurant_reviews_alter_restaurant_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuimages',
            name='img',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]