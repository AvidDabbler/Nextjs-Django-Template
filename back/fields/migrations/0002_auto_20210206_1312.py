# Generated by Django 3.1.5 on 2021-02-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='censusfields',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
