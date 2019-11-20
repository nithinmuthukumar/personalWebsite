from builtins import range

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .models import *
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views import generic
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'range'


    #override method
    def get_queryset(self):
        return [i for i in range(10)]
class FeedbackView(generic.FormView):
    pass
class ResumeView(generic.ListView):
    template_name ="resume.html"
    context_object_name = 'achievements'
def resume(request):
    template = loader.get_template('resume.html')
    context = {
        'achievements': Achievement.objects.values(),'skills':Skill.objects.values(),
        'clubs':Club.objects.values(),'projects':Project.objects.values()
    }
    return HttpResponse(template.render(context, request))


