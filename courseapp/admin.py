from django.contrib import admin

from .models import (
    CourseModel, 
    QuestionModel,
    McqQuestionModel,
    SubQuestionModel,
    )
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(CourseModel, CourseAdmin)
admin.site.register(QuestionModel, CourseAdmin)
admin.site.register(McqQuestionModel, CourseAdmin)
admin.site.register(SubQuestionModel, CourseAdmin)