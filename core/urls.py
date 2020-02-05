from django.urls import path
from .views import (item_list, about_us)

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
    path('about_us/', about_us, name='about_us'),
]
