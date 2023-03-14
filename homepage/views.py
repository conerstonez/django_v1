from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'homepage/index.html')


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result = val1 + val2
    return render(request, 'post/hello.html', {'result': result})
