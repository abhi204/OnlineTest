from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from useraccount.decorators import admin_required
from courseapp.models import QuestionModel

from .forms import McqQuestionForm, SubQuestionForm
# Create your views here.

@login_required
@admin_required
def question_list_view(request, course_name):
    questions = QuestionModel.objects.filter(course_id=course_name)
    if request.method == "POST" and request.POST['method']=="PUT":
        instance = QuestionModel.objects.get(q_id=request.POST["q_id"])
        print(instance)
        print(request.POST)
        if request.POST['qtype']=='mcq':
            instance = instance.mcqquestionmodel
            question_form = McqQuestionForm(request.POST, instance=instance)
        else:
            instance = instance.subquestionmodel
            question_form = SubQuestionForm(request.POST, instance=instance)
        if question_form.is_valid():
            question_form.save()
        else:
            HttpResponse(question_form.errors)
            
    return render(request,'question/questions.html',{"questions": questions, "course": course_name})