from django.db import models

# Create your models here.

class CourseModel(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name="Course ID")
    name = models.CharField(max_length=100, unique=True, verbose_name="Course Name")
    content = models.CharField(max_length=255, verbose_name="Course Content")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name    