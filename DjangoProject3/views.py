from django.shortcuts import *
from .settings import DEBUG

def port(request):
    return render(request, 'port.html')

def about(request):
    return render(request, 'about.html')
def projects(request):
    return render(request, 'Projects.html')