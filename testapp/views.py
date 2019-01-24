from django.shortcuts import render, Http404
from courseapp.models import CourseModel

from django.contrib.auth.decorators import login_required
from useraccount.decorators import admin_required

# Create your views here.

@login_required
@admin_required
def test_detail(request, course_name):
    try:
        course_instance = CourseModel.objects.get(name=course_name)
    except CourseModel.DoesNotExist:
        raise Http404("There is no course that matches user's query")
    return render(request, 'testapp/test-details.html',{'course': course_instance})
