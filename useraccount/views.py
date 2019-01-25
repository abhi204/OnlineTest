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
from courseapp.models import CourseModel


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

def candidate_login_view(request):
    if request.method == 'POST':
        mobile = request.POST['candidate-phone']
        password = request.POST['candidate-password']
        user = authenticate(request,mobile=mobile,password=password)
        if user is not None:
            django_login(request, user)
            return HttpResponse(**SUCCESS_RESPONSE)
        else:
            return HttpResponse(json.dumps({'error':'Invalid Login Credentials'}),content_type="application/json")
    else:
        return render(request, "useraccount/user-login.html")


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

def select_course(request):
    if request.method == "POST":
        selected_course = request.POST['selected_course']

    else:
        courses = CourseModel.objects.all()
        candidate_name = request.user.full_name
        candidte_email = request.user.email
        return render(request, "useraccount/select-course.html", {"candidate-name": candidate_name, "courses": courses})

