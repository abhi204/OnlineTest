from django.shortcuts import render, Http404, HttpResponse
from django.http import JsonResponse
from courseapp.models import CourseModel
from .models import TestModel
from courseapp.models import McqQuestionModel, SubQuestionModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from useraccount.decorators import admin_required
from django.utils import timezone
from datetime import timedelta
from .functions import get_score
import json

import random
# Create your views here.

@login_required
def test_detail(request, course_name):
    try:
        course_instance = CourseModel.objects.get(name=course_name)
    except CourseModel.DoesNotExist:
        raise Http404("There is no course that matches user's query")
    return render(request, 'testapp/test-details.html',{'course': course_instance})

@login_required
@csrf_exempt
def take_test(request, course_name):
    #if request.method == "GET":
    #    instance, created = TestModel.objects.get_or_create(
    #        course_id=course_name,
    #        candidate_id=request.user.email,
    #        defaults={
    #            "candidate_id": request.user.email,
    #            "course_id": course_name,
    #        })
    #    if not created:
    #        instance.test_start_time = timezone.now()
    #        instance.score = 0
    #    instance.save()
    #    return render(request, "testapp/test.html", {"course": course_name})
    if request.method == "GET":
        instance = TestModel.objects.filter(course_id=course_name, candidate_id=request.user.email).exists()
        if not instance:
            instance_create = TestModel.objects.create(course_id=course_name, candidate_id=request.user.email)
            instance_create.save()
            return render(request, "testapp/test.html", {"course": course_name})
        else:
            return render(request, "testapp/test_taken.html", {"course": course_name})
    if request.method == "POST":
        answers = json.loads(request.body)
        instance, created = TestModel.objects.get_or_create(course_id=course_name, candidate_id=request.user.email)
        if created:
            return JsonResponse({"response": "Operation Not Allowed"})
        #check time (raise error if fail)
        start_time = instance.test_start_time
        current_time = timezone.now()
        if current_time - start_time > timedelta(seconds=1830):
            return JsonResponse({"response":"Time Limit Exceeded"})
        #do evaluation
        score = get_score(answers)
        #store in db
        instance.score = score
        instance.save()
        #redirect to score page (if permits)
        return JsonResponse({"response": "success", "score": score })

@login_required
def get_questions(request,course_name):
    if request.method == "GET":
        sub_questions_all = list(SubQuestionModel.objects.values('question', 'q_id').filter(course_id=course_name))
        mcq_questions_all = list(McqQuestionModel.objects.values(
            'question',
            'q_id',
            'opt_a',
            'opt_b',
            'opt_c',
            'opt_d',
        ).filter(course_id=course_name))
        all_questions = mcq_questions_all
        all_questions.extend(sub_questions_all)
        questions_random = random.sample(all_questions,30 if len(all_questions)>30 else len(all_questions))

        return JsonResponse(questions_random, safe=False)


def select_course(request):
    if request.method == "POST":
        pass
    else:
        courses = CourseModel.objects.all()
        candidate_name = request.user.full_name
        candidte_email = request.user.email
        return render(request, "select-course.html", {"candidate-name": candidate_name, "courses": courses})


def test_result(request, course_name):
    test_result_instance = TestModel.objects.get(course_id=course_name, candidate_id=request.user.email)
    if request.method == "GET":
        return render(request, 'testapp/test-result.html', {'result': test_result_instance})
