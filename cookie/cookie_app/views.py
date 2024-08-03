from django.http import HttpResponse

def track_visits(request):
    # Get the number of visits from the cookie, default to 0 if not set
    visits = int(request.COOKIES.get('visits', '0'))
    
    # Increment the visit count
    visits += 1
    
    # Create a response and set the updated visit count in the cookie
    response = HttpResponse(f"Number of visits: {visits}")
    response.set_cookie('visits', visits)
    
    return response
