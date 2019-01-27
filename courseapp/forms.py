from django.forms import ModelForm
from .models import CourseModel

class CourseForm(ModelForm):
    class Meta:
        model = CourseModel
        fields = ['name', 'description', 'content']