# Generated by Django 2.2.7 on 2019-11-23 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitra', '0007_auto_20191121_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iklan',
            name='jenis_kendaraan',
            field=models.CharField(choices=[('sepeda_motor', 'Sepeda Motor'), ('mobil', 'Mobil')], max_length=20),
        ),
    ]