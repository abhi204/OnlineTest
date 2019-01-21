from django.contrib import admin

from .models import CourseModel, QuestionModel
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(CourseModel, CourseAdmin)
admin.site.register(QuestionModel, CourseAdmin)