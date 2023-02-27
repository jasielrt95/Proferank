from django.urls import path

from .views import (
    ConfessionFeedView,
    ConfessionDetailView,
    ConfessionLikeView,
    ConfessionDislikeView,
    ConfessionCreateView,
)

app_name = "confessions"

urlpatterns = [
    path("", ConfessionFeedView.as_view(), name="confession_feed"),
    path("<int:pk>/", ConfessionDetailView.as_view(), name="confession_detail"),
    path("create/", ConfessionCreateView.as_view(), name="confession_create"),
    path("<str:college>/", ConfessionFeedView.as_view(), name="confession_feed"),
    path("<int:pk>/like", ConfessionLikeView, name="confession_like"),
    path("<int:pk>/dislike", ConfessionDislikeView, name="confession_dislike"),
]
