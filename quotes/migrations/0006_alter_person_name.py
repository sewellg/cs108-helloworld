# Generated by Django 4.0.3 on 2022-03-30 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_quote_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.TextField(),
        ),
    ]
