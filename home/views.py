from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from useraccount.decorators import admin_required
# Create your views here.

decorators = [login_required, admin_required]

@method_decorator(decorators, name='get')
class DashBoardView(TemplateView):
    template_name = "dashboard.html"

    def get(self,request):
        return render(request,self.template_name)

