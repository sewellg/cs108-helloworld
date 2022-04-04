##### quotes/views.py #####

from .models import Quote, Person
from django.views.generic import ListView, DetailView, CreateView, UpdateView
import random
from .forms import CreateQuoteForm, UpdateQuoteForm
from django.views.generic.edit import DeleteView  
from django.urls import reverse 

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
    context_object_name = 'person'

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
