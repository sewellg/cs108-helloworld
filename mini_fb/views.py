from ast import Delete
import profile
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, StatusMessage
from.forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone

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

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context

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

def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            status_message.timestamp = timezone.now()

        

            # now commit to database
            status_message.save()

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)

class DeleteStatusMessageView(DeleteView):
    template_name = "mini_fb/delete_status_form.html"
    model = StatusMessage
    

    def get_object(self):
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']
        st_msg = StatusMessage.objects.get(pk=status_pk)

        return st_msg

    def get_success_url(self):
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']
        url = reverse('show_profile_page', kwargs={'pk': profile_pk})
        return url
    def get_context_data(self, **kwargs):
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['st_msg'] = st_msg
        return context
# Create your views here.
