from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World..!")
    # return render(request, 'index.html', {'name': 'Mosh'})    