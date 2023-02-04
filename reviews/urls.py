from django.urls import path


from .views import ReviewFormView, SuggestionsFormView

app_name = "reviews"

urlpatterns = [
    path("review/<int:pk>", ReviewFormView.as_view(), name="rate_course"),
    path("suggestions", SuggestionsFormView.as_view(), name="suggestions"),
]
