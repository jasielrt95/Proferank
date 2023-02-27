from django.urls import path

from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseCodificationUpdateView,
)

app_name = "courses"

urlpatterns = [
    path("all", CourseListView.as_view(), name="all_courses"),
    path("<int:pk>", CourseDetailView.as_view(), name="specific_course"),
    path("create", CourseCreateView.as_view(), name="create_course"),
    path(
        "update/<int:pk>",
        CourseCodificationUpdateView.as_view(),
        name="add_course_codification",
    ),
]
