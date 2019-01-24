from django.urls import path
from . import views

urlpatterns = [
    path('details/<str:course_name>',views.test_detail),
    path('<str:course_name>', views.test_start),
]