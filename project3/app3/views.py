from django.http import HttpResponse
import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body><h1>It is now %s </h1></body></html>" % now
    return HttpResponse(html)