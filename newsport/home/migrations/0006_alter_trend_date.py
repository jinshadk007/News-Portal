# Generated by Django 4.2 on 2023-04-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_trend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='date',
            field=models.DateField(),
        ),
    ]
