from django.shortcuts import render
from useraccount.decorators import admin_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
@admin_required
def course_list_view(request):
    if request.method == 'GET':
        return render(request,"courses.html")

@login_required
@admin_required
def candidate_list_view(request):
    if request.method == 'GET':
        return render(request,"candidates.html")