from django.urls import path
from . import views

urlpatterns = [
    path('details/<str:course_name>',views.test_detail),
    path('<str:course_name>', views.take_test),
    path('questions/<str:course_name>',views.get_questions),
    path('result/<str:course_name>',views.test_result),
]