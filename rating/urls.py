from django.urls import path
from . import views

from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60*60*8)(views.main)),
    path('<str:course_name>', cache_page(60*60*8)(views.course)),
    path('prof/<str:prof>', views.professor),
    path('register/RsGH2Qs23', views.register),
    path('register/sdfsgFwefsfg32dsF', views.register_courses_details),
    path('email/', views.check_mail),
    path('register/fsdfEF23dsf3r224dsF', views.update_course_description),

]