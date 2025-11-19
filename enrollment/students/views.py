from django.shortcuts import render
from django.http import HttpResponse

def students(request):
  return HttpResponse("Hello Students")

def students2(request):
  return HttpResponse("This it the student project app")

def students3(request):
  return HttpResponse("Welcome!")


# Create your views here.
