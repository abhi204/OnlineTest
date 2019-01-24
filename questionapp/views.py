from django.shortcuts import render, HttpResponse, redirect, Http404
from django.contrib.auth.decorators import login_required
from useraccount.decorators import admin_required
from courseapp.models import QuestionModel
from uuid import uuid4

from .forms import McqQuestionForm, SubQuestionForm
# Create your views here.

@login_required
@admin_required
def question_list_view(request, course_name):
    questions = QuestionModel.objects.filter(course_id=course_name)
    if request.method == "POST" and request.POST.get('method',False):
        instance = QuestionModel.objects.get(q_id=request.POST["q_id"])
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
    elif request.method == "POST":
        q_id = 'Q'+str(uuid4()).split('-')[0]
        data = request.POST.copy()
        data.update(q_id=q_id)
        if data['qtype']=='mcq':
            question_form = McqQuestionForm(data)
        else:
            question_form = SubQuestionForm(data)
        if question_form.is_valid():
            question_form.save()
        else:
            return render(request,'question/questions.html',{"questions": questions, "course": course_name, "errors": question_form.errors})
            
    return render(request,'question/questions.html',{"questions": questions, "course": course_name})


@login_required
@admin_required
def delete_question(request, q_id):
    try:
        instance = QuestionModel.objects.get(q_id=q_id)
    except QuestionModel.DoesNotExist:
        raise Http404("No Question Matches the current query")
    instance.delete()
    return redirect(request.META.get('HTTP_REFERER', '/course/course-list'))