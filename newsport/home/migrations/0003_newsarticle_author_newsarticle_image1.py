# Generated by Django 4.2 on 2023-04-11 06:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_newsarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='image1',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image'),
            preserve_default=False,
        ),
    ]