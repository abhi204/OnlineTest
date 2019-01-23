from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('course-list/',views.course_list_view,name="course_list"),
    path('candidate-list/', views.candidate_list_view,name="candidate_list"),

]