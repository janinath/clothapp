# Generated by Django 4.2.7 on 2023-12-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(db_column='image', null=True, upload_to='dresses'),
        ),
    ]
