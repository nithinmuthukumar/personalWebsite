from django.urls import path

from . import views

from django.urls import path

from . import views
from django.urls import path

from . import views

app_name = 'about'
urlpatterns = [
    path('', views.IndexView.as_view(), name='about'),
    path('resume',views.resume,name='resume'),
    path('projects',views.projects,name='projects')
]