from django.shortcuts import render
from .models import Item

def item_list(request):
    context = {
    'items': Item.objects.all()
    }
    return render(request, 'core/home-page.html', context)

def about_us(request):
    return render(request, 'core/about_us.html')
