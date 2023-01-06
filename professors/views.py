from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Professor
from courses.models import Course
from comments.models import Course_Comment
from .forms import RateProfessorForm, CreateProfessorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ProfessorListView(ListView):
    model = Professor
    template_name = "professor_list.html"


class ProfessorDetailView(DetailView):

    model = Professor
    template_name = "professor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profesor = Professor.objects.get(id=self.kwargs["pk"])
        context["courses"] = Course.objects.filter(professor=profesor)
        # get the comments from the courses associated with the professor
        context["comments"] = Course_Comment.objects.filter(
            course__in=Course.objects.filter(professor=profesor)
        )
        context["form"] = RateProfessorForm()
        context["professor"] = profesor
        return context


class ProfessorCreateView(LoginRequiredMixin, CreateView):
    model = Professor
    template_name = "create_professor.html"
    form = CreateProfessorForm
    fields = ["first_name", "last_name", "college", "faculty"]
    success_url = reverse_lazy("professors:all_professors")
