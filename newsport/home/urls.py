from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category',views.category,name="category"),
    # path('news',views.news,name='news'),
    path('<int:id>',views.detail,name='detail'),


]