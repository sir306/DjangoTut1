from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# first view
def index(request):
    return HttpResponse('Hello World')

# second view
def item(request):
    return HttpResponse('<h1>This is an item view</h1>')