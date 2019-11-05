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
    template_name = 'about/index.html'
    context_object_name = 'names'


    #override method
    def get_queryset(self):
        return People.objects.order_by('-pub_date')[:5]
class FeedbackView(generic.FormView):
    pass