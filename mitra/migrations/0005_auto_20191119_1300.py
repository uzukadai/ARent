# Generated by Django 2.2.7 on 2019-11-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitra', '0004_auto_20191119_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iklan',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]