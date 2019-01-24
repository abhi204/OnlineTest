from django.shortcuts import render, Http404, HttpResponse
from courseapp.models import CourseModel
from .models import TestModel

from django.contrib.auth.decorators import login_required
from useraccount.decorators import admin_required

# Create your views here.

@login_required
def test_detail(request, course_name):
    try:
        course_instance = CourseModel.objects.get(name=course_name)
    except CourseModel.DoesNotExist:
        raise Http404("There is no course that matches user's query")
    return render(request, 'testapp/test-details.html',{'course': course_instance})

@login_required
def test_start(request, course_name):
    instance, created = TestModel.objects.get_or_create(
        course_id=course_name,
        candidate_id=request.user.email)
    if created:
        instance.save()
        print("Instance Saved!!!")
    return HttpResponse("TEST Begins")
