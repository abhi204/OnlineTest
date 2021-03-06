from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from useraccount.decorators import admin_required
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import CourseModel
from django.http import HttpResponse
from testapp.models import TestModel
from useraccount.models import User
# Create your views here.
@login_required
@admin_required
def course_list_view(request):
    courses = CourseModel.objects.all()
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            return render(request, "courses.html",{"courses": courses})
        else:
            print(f"errors : {course_form.errors}")
            return render(request, "courses.html", {
                    "errors": course_form.errors,
                     "courses": courses
                     })
    return render(request, "courses.html", {"courses": courses})


def course_edit_view(request):
    if request.method == 'POST':
        instance = CourseModel.objects.get(name=request.POST['name'])
        course_edit_form= CourseForm(request.POST, instance=instance)
        if course_edit_form.is_valid():
            course_edit_form.save()
            return redirect('course_list')
        else:
            print(f"errors : {course_edit_form.errors}")
            return render(request, "courses.html", {
                "errors": course_edit_form.errors,
            })


@login_required
@admin_required
def candidate_list_view(request):
    test_details = TestModel.objects.order_by('-test_start_time')
    if request.method == 'GET':
        return render(request, "candidates.html", {"test_details": test_details})

@login_required
@admin_required
def candidate_details_view(request, candidate_email):
    candidate = User.objects.get(pk=candidate_email)
    return render(request, "candidate_details.html", {"candidate": candidate})


@login_required
@admin_required
def course_delete(request,course_name):
    instance = CourseModel.objects.get(name=course_name)
    instance.delete()
    return redirect('course_list')
