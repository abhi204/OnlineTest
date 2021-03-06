from django.db import models
from useraccount.models import User
# Create your models here.


class CourseModel(models.Model):
    name = models.CharField(max_length=100, primary_key=True, verbose_name="Course Name")
    description = models.TextField(verbose_name="Course Content")
    content = models.TextField(verbose_name="Course Content")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name


class QuestionModel(models.Model):
    q_id = models.CharField(max_length=10, primary_key=True, verbose_name="Question ID")
    question = models.CharField(max_length=255)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, blank=False,)

    class Meta:
        verbose_name = "All Question"

    def __str__(self):
        return self.question

    @property
    def qtype(self):
        if len(McqQuestionModel.objects.filter(pk=self.pk)):
            return "mcq"
        return "sub"


class SubQuestionModel(QuestionModel):
    
    class Meta:
        verbose_name = "Subjective Question"
        verbose_name_plural = "Subjective Questions"


class McqQuestionModel(QuestionModel):
    opt_a = models.CharField(max_length=255, blank=False, verbose_name="Option A")
    opt_b = models.CharField(max_length=255, blank=False, verbose_name="Option B")
    opt_c = models.CharField(max_length=255, blank=False, verbose_name="Option C")
    opt_d = models.CharField(max_length=255, blank=False, verbose_name="Option D")

    class Meta:
        verbose_name = "MCQ Question"
        verbose_name_plural = "MCQ Questions"
