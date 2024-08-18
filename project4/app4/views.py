from django.http import HttpResponse
import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    html="<h1>It is now %s </h1>" % now
    return HttpResponse(html)

def four_hours_ahead(request):
    fa=datetime.datetime.now()+datetime.timedelta(hours=4)
    html="<h1>It is now %s </h1>" % fa
    return HttpResponse(html)

def four_hours_before(request):
    fb=datetime.datetime.now()+datetime.timedelta(hours=-4)
    html="<h1>It is now %s </h1>" % fb
    return HttpResponse(html)