from django.contrib import admin

from .models import CourseModel
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(CourseModel, CourseAdmin)