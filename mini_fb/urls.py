from .models import Profile
from django.urls import path
from .views import CreateProfileView, DeleteStatusMessageView, ShowAllProfilesView, ShowNewsFeedView, ShowProfilePageView, UpdateProfileView, post_status_message 

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="profiles"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('profile/<int:pk>/post_status', post_status_message, name="post_status"),
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name="delete_status"),
    path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name="news_feed"),
]
