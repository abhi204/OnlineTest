from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^course/(?P<course_name>[^/]+)/$', views.question_list_view,),
]