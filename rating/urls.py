from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('<str:course_name>', views.course),
    path('prof/<str:prof>', views.professor),
    path('register/RsGH2Qs23', views.register),
    path('register/sdfsgFwefsfg32dsF', views.register_courses_details)
]