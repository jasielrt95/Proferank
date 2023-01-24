from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course
from comments.models import Course_Comment


class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        universities = set()
        departments = set()
        for course in Course.objects.all():
            universities.add(course.professor.college)
            departments.add(course.professor.faculty)
        courses = Course.objects.all()
        context["courses"] = courses
        context["universities"] = universities 
        context["departments"] = departments
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "course.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Course.objects.get(id=self.kwargs["pk"])
        context["course"] = course
        context["professor"] = course.professor
        comments = list(Course_Comment.objects.filter(course=course))
        context["comments"] = comments
        return context
