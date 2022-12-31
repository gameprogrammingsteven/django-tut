from django.shortcuts import render
from django.http import HttpResponse

def projects(req):
    return render(req, 'projects.html')

def project(req, pk):
    return render(req, 'single-project.html')
