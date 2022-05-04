# Generated by Django 4.0.3 on 2022-04-27 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_restaurant_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='rescuisine',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rescuisine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project.cuisine'),
            preserve_default=False,
        ),
    ]