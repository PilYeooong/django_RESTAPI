# Generated by Django 2.1.7 on 2019-12-07 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_author',
            field=models.CharField(max_length=30),
        ),
    ]
