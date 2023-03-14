from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return render(request, 'post/hello.html')


def greet(request):
    return HttpResponse("Welcome to django")


def bye(request):
    return HttpResponse("Have a nice day")
