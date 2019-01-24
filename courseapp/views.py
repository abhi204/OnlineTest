<<<<<<< HEAD
from django.shortcuts import render, HttpResponse
=======
from django.shortcuts import render, redirect
>>>>>>> f6e9a1af3aba16f3bd68ed9f3b6ef4d6953fd925
from useraccount.decorators import admin_required
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import CourseModel
from django.http import HttpResponse
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
    if request.method == 'GET':
        return render(request,"candidates.html")

@login_required
@admin_required
def course_delete(request,course_name):
    instance = CourseModel.objects.get(name=course_name)
    instance.delete()
    return redirect('course_list')
