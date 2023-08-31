# middleware.py
from django.urls import resolve
from django.http import HttpResponseRedirect

class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the URL path from the request
        path = request.path_info

        try:
            # Attempt to resolve the URL
            resolve(path)
        except:
            # If the URL cannot be resolved, it's invalid
            # Redirect to a default URL or a specific URL of your choice
            return HttpResponseRedirect('/api/')

        response = self.get_response(request)
        return response