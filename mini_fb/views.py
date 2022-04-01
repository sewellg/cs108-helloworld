from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Profile
from.forms import CreateProfileForm, UpdateProfileForm

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

class CreateProfileView(CreateView):
    form_class = CreateProfileForm
    model = Profile
    template_name = "mini_fb/create_profile_form.html"
    # context_object_name = "create_profile"
    # fields = '__all__'

class UpdateProfileView(UpdateView):
    form_class = UpdateProfileForm
    model = Profile
    template_name = "mini_fb/update_profile_form.html"

# Create your views here.
