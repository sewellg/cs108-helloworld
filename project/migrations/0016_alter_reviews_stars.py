# Generated by Django 4.0.3 on 2022-05-02 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_alter_reviews_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='stars',
            field=models.CharField(choices=[('1/5', '1 Star'), ('2/5', '2 Stars'), ('3/5', '3 Stars'), ('4/5', '4 Stars'), ('5/5', '5 Stars')], default='1/5', max_length=20),
        ),
    ]
