from django.shortcuts import render

def addition(request):
    return render(request, 'index.html')
