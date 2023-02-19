from django.urls import path

from .views import ConfessionFeedView

app_name = "confessions"

urlpatterns = [
    path("", ConfessionFeedView.as_view(), name="confession_feed"),
]