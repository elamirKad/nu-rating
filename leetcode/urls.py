from django.urls import path
from . import views

from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(1)(views.main)),
    path('dfgdfgdfgfdsfgdgdfgfdgdsfg/gdfgdfgdsfd4r43fdf34', views.update),
    path('<slug:username>', views.user),
    path('add_contests/', views.add_contests),
    path('sdfsdfdsf/32rdsf42efdf', views.update_users)
]