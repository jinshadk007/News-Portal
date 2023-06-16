
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import latest, trend, slider ,category


def index(request):
    obj = slider.objects.all()
    latest_news = latest.objects.order_by('-date')[:10]
    get = trend.objects.all()
    return render(request, 'index.html', {'data': obj, 'news': latest_news, 'trend': get})


def detail(request, id):
    new = get_object_or_404(latest, pk=id)
    return render(request, 'single.html', {'news': new})


def category(request):
    cate = category.objects.filter(status=0);
    return render(request, 'category.html', {"category": cate})


# def news(request, slug):
#     if category.objects.filter(slug=slug, status=0):
#         product = news.objects.filter(category__slug=slug)
#         return render(request, 'news_category.html', {"product": product})
#     else:
#         messages.warning(request, "no")
#         return redirect('category')
