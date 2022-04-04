##### quotes/views.py #####

from .models import Quote, Person
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import random
from .forms import CreateQuoteForm, UpdateQuoteForm, AddImageForm
from django.views.generic.edit import DeleteView  
from django.urls import reverse 
from django.shortcuts import render, redirect

class HomePageView(ListView):
    '''Create a subclass of ListView to display all quotes.'''

    model = Quote # retrieve objects of type Quote from the database
    template_name = 'quotes/home.html'
    context_object_name = 'quotes' # how to find the data in the template file

class QuotePageView(DetailView):
    '''Show the details for one quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    '''Show the details for one quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    ## note: reusing same template as DetailView to show one quote!!
    context_object_name = 'quote'

    # pick one quote at random:
    def get_object(self):
        '''Return one Quote object chosen at random.'''
		
        all_quotes = Quote.objects.all()
        return random.choice(all_quotes)

class PersonPageView(DetailView):
    '''Show all quotes and all images for one person.'''

    model = Person
    template_name = 'quotes/person.html'
    # context_object_name = 'person'

    def get_context_data(self, **kwargs):
        '''Return a dictionary with context data for this template to use.'''

        # get the default context data:
        # this will include the Person record for this page view
        context = super(PersonPageView, self).get_context_data(**kwargs)

        # create add image form:
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form

        # return the context dictionary:
        return context

class CreateQuoteView(CreateView):
    '''Create a new Quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = CreateQuoteForm # which form to use to create the Quote
    template_name = "quotes/create_quote_form.html" # delegate the dispay to this template
		
class UpdateQuoteView(UpdateView):
    '''Update an existing Quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = UpdateQuoteForm # which form to use to create the Quote
    template_name = "quotes/create_quote_form.html" # delegate the display to this template

class DeleteQuoteView(DeleteView):
    '''A view to delete a quote and remove it from the database.'''

    template_name = "quotes/delete_quote.html"
    queryset = Quote.objects.all()

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''

        # get the pk for this quote
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first() # get one object from QuerySet
        
        # find the person associated with the quote
        person = quote.person

        # reverse to show the person page
        return reverse('person', kwargs={'pk':person.pk})

def add_image(request, pk):
    '''A custom view function to handle the submission of an image upload.'''

    # find the person for whom we are submitting the image
    person = Person.objects.get(pk=pk)

    # read request data into AddImageForm object
    form = AddImageForm(request.POST or None, request.FILES or None)

    # check if the form is valid, save object to database
    if form.is_valid():

        image = form.save(commit=False) # create the Image object, but not save yet

        # attach the foreign key to this image
        image.person = person
        image.save() # store to the database

    else:
        print("Error: the form was not valid.")

    # redirect to a new URL, display person page
    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)
