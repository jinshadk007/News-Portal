# Generated by Django 4.2 on 2023-04-17 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='image')),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('news_image', models.ImageField(upload_to='image')),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('profile', models.ImageField(upload_to='image')),
                ('author', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
