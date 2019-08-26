from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('welcom to Index')

def student(request):
    return HttpResponse('')

def degree(request):
    return HttpResponse('')