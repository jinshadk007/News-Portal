# Generated by Django 4.2 on 2023-04-12 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_newsarticle_latest'),
    ]

    operations = [
        migrations.CreateModel(
            name='trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('name', models.CharField(max_length=60)),
            ],
        ),
    ]
