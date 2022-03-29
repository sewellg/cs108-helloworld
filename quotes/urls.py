##### quotes/urls.py #####

from django.urls import path
from .views import HomePageView, PersonPageView, QuotePageView, RandomQuotePageView

urlpatterns = [
    # map the URL (empty string) to the view
    path('all', HomePageView.as_view(), name='all'), # generic class-based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), # show one quote by its primary key
    path('', RandomQuotePageView.as_view(), name='random'),  # show one quote at random
    path('person/<int:pk>', PersonPageView.as_view() name="person"),
]