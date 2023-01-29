from django.urls import path

from .views import CourseCommentCreateView

app_name = "comments"

urlpatterns = [
    path(
        "course/<int:pk>/comment",
        CourseCommentCreateView.as_view(),
        name="course_comment",
    ),
]
