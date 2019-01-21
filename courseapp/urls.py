from django.urls import path, include
from . import views

urlpatterns = [
    path('list/',views.course_list_view,name="course_list"),
]