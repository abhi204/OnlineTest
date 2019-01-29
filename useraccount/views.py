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
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .models import User
from django.core.mail import send_mail


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
            if user.active == True:
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
            user = signup_form.save(commit=False)
            user.is_active = False

            current_site = get_current_site(request)
            mail_subject = 'Activate your user account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = signup_form.cleaned_data.get('email')
            send_mail(mail_subject, message,'evolettech@gmail.com', [to_email,])
            user.save()
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


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # if user is not None and account_activation_token.check_token(user, token):

    if user is not None:
        user.active = True
        user.save()
        django_login(request, user)
        return redirect('candidate_login')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse(user)

