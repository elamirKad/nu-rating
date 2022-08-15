from django.urls import path
from . import views

from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(30)(views.main)),
    path('dfgdfgdfgfdsfgdgdfgfdgdsfg/gdfgdfgdsfd4r43fdf34', views.update)
]