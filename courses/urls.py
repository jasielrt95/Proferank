from django.urls import path

from .views import CourseListView, CourseDetailView, CourseCreateView

app_name = "courses"

urlpatterns = [
    path("all", CourseListView.as_view(), name="all_courses"),
    path("<int:pk>", CourseDetailView.as_view(), name="specific_course"),
    path("professor/<int:pk>/course", CourseCreateView.as_view(), name="create_course_for_professor"),
    path("create", CourseCreateView.as_view(), name="create_course"),
]
