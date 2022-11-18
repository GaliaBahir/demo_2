from django.shortcuts import render
import django.http as Http

def counter(request):
    counter = 1
    return render(request, 'counter.html', {'counter': counter})