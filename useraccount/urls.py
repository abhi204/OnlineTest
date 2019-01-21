from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('register/',TemplateView.as_view(template_name="useraccount/register.html")),
    path("create/candidate",views.signup_view,name="signup")
]