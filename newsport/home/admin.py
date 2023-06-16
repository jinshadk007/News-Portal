from category import Category
from django.contrib import admin
from .models import slider, latest, trend, category,news

admin.site.register(slider)
admin.site.register(latest)
admin.site.register(trend)
admin.site.register(category)
admin.site.register(news)
# Register your models here.
