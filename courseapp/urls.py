from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('course-list/',views.course_list_view,name="course_list"),
    path('candidate-list/', views.candidate_list_view,name="candidate_list"),
    path('course-edit/',views.course_edit_view,name="course_edit"),
    path('delete/<str:course_name>',views.course_delete),
    re_path(r'^candidate/(?P<candidate_email>[^/]+)/$', views.candidate_details_view, name="candidate"),

]