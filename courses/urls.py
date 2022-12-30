from django.urls import path

from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('all', CourseListView.as_view()),
    path('<int:pk>', CourseDetailView.as_view(), name='specific_course'),
]