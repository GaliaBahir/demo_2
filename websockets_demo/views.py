from django.shortcuts import render

def counter(request):
    return render(request, 'counter.html')
