from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('<str:course_name>', views.course),
    path('prof/<str:prof>', views.professor),
]