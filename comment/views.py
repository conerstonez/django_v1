from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def first_comment(request):
    return render(request, 'comment/comment.html')


def greet(request):
    return HttpResponse("thanks for your opinion")
