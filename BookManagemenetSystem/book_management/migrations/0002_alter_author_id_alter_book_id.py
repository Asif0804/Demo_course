# Generated by Django 4.2.8 on 2023-12-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.IntegerField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
