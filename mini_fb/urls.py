from django.urls import path
from .views import CreateProfileView, ShowAllProfilesView, ShowProfilePageView, UpdateProfileView

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="profiles"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile")
]
