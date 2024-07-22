from django.shortcuts import render

def greet_user(request,s):
    return render(request, "index.html",{"user":s})