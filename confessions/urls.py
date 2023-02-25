from django.urls import path

from .views import ConfessionFeedView, ConfessionDetailView

app_name = "confessions"

urlpatterns = [
    path("", ConfessionFeedView.as_view(), name="confession_feed"),
    path("<int:pk>/", ConfessionDetailView.as_view(), name="confession_detail"),
]
