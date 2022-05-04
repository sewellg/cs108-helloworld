# Generated by Django 4.0.3 on 2022-05-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_alter_reviews_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='stars',
            field=models.CharField(choices=[('One', '1 Star'), ('Two', '2 Stars'), ('Three', '3 Stars'), ('Four', '4 Stars'), ('Five', '5 Stars')], default='One', max_length=20),
        ),
    ]
