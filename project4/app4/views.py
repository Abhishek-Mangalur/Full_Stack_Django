from django.http import HttpResponse
import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    html="<h1>It is now %s </h1>" % now
    return HttpResponse(html)

def fhrsa(request):
    fa=datetime.datetime.now() + datetime.timedelta(hours=4)
    html="<h1>Four Hours ahead Time is: %s </h1>" % fa
    return HttpResponse(html)

def fhrsb(request):
    fb=datetime.datetime.now() + datetime.timedelta(hours=-4)
    html="<h1>Fours Hours before Time is: %s </h1>" % fb
    return HttpResponse(html)