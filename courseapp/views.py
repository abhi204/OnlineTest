from django.shortcuts import render, HttpResponse
from useraccount.decorators import admin_required
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import CourseModel

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


@login_required
@admin_required
def candidate_list_view(request):
    if request.method == 'GET':
        return render(request,"candidates.html")
