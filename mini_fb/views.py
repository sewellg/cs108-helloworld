from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile

class ShowAllProfilesView(ListView):
    '''show a listing of profiles'''
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"

class ShowProfilePageView(DetailView):
    '''shows a detailed profile'''
    model = Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "profile"

# Create your views here.
