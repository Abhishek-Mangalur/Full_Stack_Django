from django.shortcuts import render
from django.http import HttpResponse

import datetime
def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body><h1>It is now %s </h1></body></html>" % now
    return HttpResponse(html)

def fhrsa(request):
    fa=datetime.datetime.now() + datetime.timedelta(hours=4)
    html="<html><body><h1> Four Hours ahead time is %s </h1></body></html>" % fa
    return HttpResponse(html)

def fhrsb(request):
    fb=datetime.datetime.now() + datetime.timedelta(hours=-4)
    html="<html><body><h1>Fours Hours before time is %s </h1></body></html>" % fb
    return HttpResponse(html)