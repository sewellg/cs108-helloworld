# Generated by Django 4.0.3 on 2022-03-28 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_image_person_remove_quote_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quotes.person'),
            preserve_default=False,
        ),
    ]
