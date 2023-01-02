from django.urls import path

from .views import CourseListView, CourseDetailView

app_name = 'courses'

urlpatterns = [
    path('all', CourseListView.as_view(), name='all_courses'),
    path('<int:pk>', CourseDetailView.as_view(), name='specific_course'),
]