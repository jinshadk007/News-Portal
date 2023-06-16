from django.db import models


class slider(models.Model):
    date = models.DateTimeField()
    image = models.ImageField(upload_to='image')
    description = models.TextField()


# Create your models here.
class latest(models.Model):
    image = models.ImageField(upload_to='image')
    category = models.CharField(max_length=50)
    date = models.DateTimeField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    image1 = models.ImageField(upload_to='image')
    author = models.CharField(max_length=50)


class trend(models.Model):
    image = models.ImageField(upload_to='image')
    category = models.CharField(max_length=50)
    date = models.DateField()
    name = models.CharField(max_length=60)


class category(models.Model):
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to='image', null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default,1=Hidden")

    def __str__(self):
        return self.name


class news(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    news_image = models.ImageField(upload_to='image', null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    profile = models.ImageField(upload_to='image', null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default,1=Hidden")

    def __str__(self):
        return self.name
