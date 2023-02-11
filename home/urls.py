from django.urls import path
from .views import IndexView, AboutView, ProfileView

app_name = "home"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about", AboutView.as_view(), name="about"),
    path("profile", ProfileView.as_view(), name="profile"),
]
