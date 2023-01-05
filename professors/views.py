from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Professor


class ProfessorListView(ListView):
    model = Professor
    template_name = "professor_list.html"


class ProfessorDetailView(DetailView):

    model = Professor
    template_name = "professor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profesor = Professor.objects.get(id=self.kwargs["pk"])
        context["professor"] = profesor
        return context
