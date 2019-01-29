from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('register/',TemplateView.as_view(template_name="useraccount/register.html"),name="register-candidate"),
    path("create/candidate",views.signup_view,name="signup"),
    path("admin-login/",views.admin_login_view,name="admin_login"),
    path("logout",views.logout_view,name="logout"),
    path("candidate-login/", views.candidate_login_view, name="candidate_login"),
    path('courses/', views.select_course,name="select_course"),
    path('success/', TemplateView.as_view(template_name="useraccount/success.html"),name="reg-success"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]