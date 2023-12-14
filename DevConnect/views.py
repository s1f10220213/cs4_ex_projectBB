from django.shortcuts import render

def project(request):
    return render(request, "DevConnect/project.html")

def projectin(request, project_name):
    return render(request, "DevConnect/projectin.html", {"project_name": project_name})