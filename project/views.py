from django.shortcuts import render
from .models import Projects
# Create your views here.
def project_list(request):
    projects = Projects.objects.all()
    print(projects)
    context = {'projects':projects}
    return render(request, 'Projects.html', context)

def project_detail(request):
    project = Projects.objects.get(id=1)
    print(project)
    context = {'project':project}
    return render(request, 'Project.html', context)