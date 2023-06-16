# Generated by Django 4.2 on 2023-04-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_trend_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('cat_name', models.CharField(max_length=50)),
                ('news_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('bub_date', models.DateField()),
                ('auther', models.CharField(max_length=50)),
            ],
        ),
    ]