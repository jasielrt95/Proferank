from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View, CreateView
from .models import Course
from comments.models import Course_Comment
from django.urls import reverse
from professors.models import Professor
from reviews.models import Review


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
        user_commented = False
        user_rated  = False
        if self.request.user.is_authenticated:
            user_commented = Course_Comment.objects.filter(
                course=course, user=self.request.user
            ).exists()
            user_rated = Review.objects.filter(
                course=course, user=self.request.user
            ).exists()
        context["user_rated"] = user_rated
        context["user_commented"] = user_commented
        context["course"] = course
        context["professor"] = course.professor
        comments = list(Course_Comment.objects.filter(course=course))
        context["comments"] = comments
        return context
    
class CourseCreateView(CreateView):
    model = Course
    template_name = "create_course.html"
    fields = ["name", "codification"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.professor = Professor.objects.get(id=self.kwargs["pk"])
        form.save()
        return redirect("courses:specific_course", pk=form.instance.pk)
    
    def form_invalid(self, form):
        return render(self.request, "create_course.html", {"form": form})
    
    