from django.shortcuts import render
import django.http as Http

def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Mosh'})
