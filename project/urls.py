from .views import *
from django.urls import path

urlpatterns = [

    path('projects/', project_list, name='project'),
]
