from django.urls import path
from .views import DeleteReviewView, SearchResultsView, ShowAllRestaurantsView, ShowMenuView, ShowRestaurantView, post_review

urlpatterns = [
    path('', ShowAllRestaurantsView.as_view(), name="restaurants"),
    path('restaurant/<int:pk>', ShowRestaurantView.as_view(), name="show_restaurant"),
    path('restaurant/menu/<int:pk>', ShowMenuView.as_view(), name="restaurant_menu"),
    path('restaurant/<int:pk>/post_review', post_review, name="post_review"),
    path('search_results', SearchResultsView.as_view(), name="search"),
    path('restaurant/<int:Restaurant_pk>/delete_review/<int:Reviews_pk>', DeleteReviewView.as_view(), name="delete_review"),
]   
