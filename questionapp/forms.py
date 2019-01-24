from django.forms import ModelForm
from courseapp.models import SubQuestionModel, McqQuestionModel

class SubQuestionForm(ModelForm):
    class Meta:
        model = SubQuestionModel
        fields = '__all__'

class McqQuestionForm(ModelForm):
    class Meta:
        model = McqQuestionModel
        fields = '__all__'