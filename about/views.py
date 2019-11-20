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
class AchievementView(generic.ListView):
    template_name ="achievement.html"
    context_object_name = 'achievements'
    model=Achievement
    def get_queryset(self):
        return Achievement.objects.values()

