from ast import Delete
from django.shortcuts import render
from .models import Restaurant, Cuisine, Customer, Menu_item, Reviews
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from .forms import CreateReviewForm
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class ShowAllRestaurantsView(ListView):
    '''shows a listing of all restaurants within 5 miles of BU's campus'''
    model = Restaurant
    template_name = "project/show_all_restaurants.html"
    context_object_name = "restaurants"

class ShowRestaurantView(DetailView):
    '''shows an individual restaurant'''
    model = Restaurant
    template_name = "project/show_restaurant.html"
    context_object_name = "Restaurant"

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowRestaurantView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateReviewForm() 
        context['create_review_form'] = form
        # return this context dictionary
        return context

class ShowMenuView(DetailView):
    '''shows a restaurants menu'''
    model = Restaurant
    template_name = "project/restaurant_menu.html"
    context_object_name = "restaurant"


def post_review(request, pk):
    '''Process a form submission to post a new review'''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        form = CreateReviewForm(request.POST or None, request.FILES or None)

        if form.is_valid():
 
            review = form.save(commit=False) # don't commit to database yet

            restaurant = Restaurant.objects.get(pk=pk)

            review.restaurant = restaurant

            review.save()

    url = reverse('show_restaurant', kwargs={'pk': pk})
    return redirect(url)

class SearchResultsView(ListView):
    '''shows all search results'''
    model = Restaurant
    template_name = "project/search_results.html"
    context_object_name = "search"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Restaurant.objects.filter(name__icontains=query)

class DeleteReviewView(DeleteView):
    template_name = "project/delete_review.html"
    model = Reviews

    def get_object(self):
        # read the URL data values into variables
        reviews_pk = self.kwargs['Reviews_pk']
        rvw = Reviews.objects.get(pk=reviews_pk)

        return rvw

    def get_success_url(self):
        # read the URL data values into variables
        restaurant_pk = self.kwargs['Restaurant_pk']
        reviews_pk = self.kwargs['Reviews_pk']
        url = reverse('show_restaurant', kwargs={'pk': restaurant_pk})
        return url
    def get_context_data(self, **kwargs):
        context = super(DeleteReviewView, self).get_context_data(**kwargs)
        rvw = Reviews.objects.get(pk=self.kwargs['Reviews_pk'])
        context['rvw'] = rvw
        return context