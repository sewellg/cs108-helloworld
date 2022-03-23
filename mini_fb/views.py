from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

class HomePageView(ListView):
    '''show a listing of quotes'''
    model = Profile
    template_name = "mini_fb/home.html"
    context_object_name = "profiles"

# Create your views here.
