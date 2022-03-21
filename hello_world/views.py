from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    '''Respond to an HTTP request with a simple web page.'''
    return HttpResponse("Hello, world!")

# Create your views here.
