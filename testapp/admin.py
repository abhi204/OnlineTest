from django.contrib import admin
from .models import TestModel

# Register your models here.
class TestAdmin(admin.ModelAdmin):
    pass

admin.site.register(TestModel, TestAdmin)