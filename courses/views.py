from django.views.generic import ListView, DetailView, CreateView
from .models import Course
from comments.models import Course_Comment
from professors.models import Professor
from reviews.models import Review
from django.contrib.auth.mixins import LoginRequiredMixin
from professors.views import ProfessorDetailView
from django.shortcuts import redirect


class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"
    context_object_name = "courses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["universities"] = set(
            Professor.objects.values_list("college", flat=True)
        )
        context["departments"] = set(
            Professor.objects.values_list("faculty", flat=True)
        )
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "course.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user_commented = Course_Comment.objects.filter(
                course=self.object, user=self.request.user
            ).exists()
            user_rated = Review.objects.filter(
                course=self.object, user=self.request.user
            ).exists()

        context["user_rated"] = (
            user_rated if self.request.user.is_authenticated else False
        )
        context["user_commented"] = (
            user_commented if self.request.user.is_authenticated else False
        )
        context["comments"] = list(Course_Comment.objects.filter(course=self.object))
        return context


class CourseCreateView(CreateView, LoginRequiredMixin):
    model = Course
    fields = ["name", "codification", "professor"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect("courses:specific_course", pk=form.instance.pk)

    def form_invalid(self, form):
        return redirect("professors:specific_professor", pk=form.instance.professor.pk)
