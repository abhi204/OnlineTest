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
def admin_login_view(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        password = request.POST['password']
        user = authenticate(request,mobile=mobile,password=password)
        if user is not None and user.is_admin:
            django_login(request,user)
            return HttpResponse(**SUCCESS_RESPONSE)
        else:
            return HttpResponse(json.dumps({'error':'Invalid Login Credentials'}),content_type="application/json")
    else:
        return redirect('homepage')

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