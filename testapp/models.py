from django.db import models
from useraccount.models import User
from courseapp.models import CourseModel

# Create your models here.
class TestModel(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, verbose_name="Test Score")
    test_start_time = models.DateTimeField(verbose_name="Start Date", auto_now=True)

    class Meta:
        verbose_name = "Test Details"
        verbose_name_plural = "Test Details"

    def __str__(self):
        return self.candidate.full_name