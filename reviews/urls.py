from django.urls import path


from .views import ReviewFormView

app_name = "reviews"

urlpatterns = [
    path("<int:pk>", ReviewFormView.as_view(), name="rate_course"),
]
