# Generated by Django 4.2.3 on 2023-09-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='images',
            field=models.ImageField(upload_to='photos/chobi'),
        ),
    ]
