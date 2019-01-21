from OnlineTest.settings import SUCCESS_RESPONSE
import json
from django.shortcuts import (
    render,
    redirect,
    HttpResponse
)
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout
)
from .forms import SignUpForm


# Create your views here.
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request,username=username,password=password)
#         if user is not None:
#             django_login(request,user)
#             return HttpResponse(**SUCCESS_RESPONSE)
#         else:
#             #change below to response=error, error = Invalid login creds
#             return HttpResponse(json.dumps({'response':'Invalid Login Credentials'}),content_type="application/json")
#     else:
#         return redirect('index')

def signup_view(request):
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return HttpResponse(**SUCCESS_RESPONSE)
        else:
            errors = signup_form.errors
            return HttpResponse(
                json.dumps({'response':'error', 'errors':errors}),
                content_type="application/json"
                )

def logout_view(request):
    django_logout(request)
    return redirect('/')