from django.views.generic import ListView, DetailView, CreateView
from .models import Professor
from courses.models import Course
from comments.models import Course_Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ProfessorListView(ListView):
    model = Professor
    template_name = "professor_list.html"
    context_object_name = "professors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = set(
            Professor.objects.values_list("department", flat=True)
        )
        context["universities"] = set(
            Professor.objects.values_list("college", flat=True)
        )
        return context


class ProfessorDetailView(DetailView):

    model = Professor
    template_name = "professor.html"
    context_object_name = "professor"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.filter(professor=self.object.pk)
        context["comments"] = Course_Comment.objects.filter(
            course__in=Course.objects.filter(professor=self.object.pk)
        )
        return context


class ProfessorCreateView(LoginRequiredMixin, CreateView):
    model = Professor
    template_name = "create_professor.html"
    fields = ["first_name", "last_name", "college", "department"]
    success_url = reverse_lazy("professors:all_professors")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["departments"] = ["Arte", "Arquitectura", "Ciencias Agrícolas", "Ciencias Ambientales", "Ciencias Físicas", "Ciencias Computadoras","Ciencias Sociales", "Ciencias Veterinarias", "Comunicación", "Derecho", "Educación", "Enfermería", "Ingeniería", "Medicina", "Música", "Odontología", "Humanidades", "Biologia", "Química", "Física", "Matemáticas", "Otro"]

        context["universities"] = ["UPR Río Piedras", "UPR Mayagüez", "UPR Arecibo", "UPR Ponce", "UPR Ciencias Medicas", "UPR Carolina", "UPR Cayey", "UPR Humacao", "UPR Aguadilla", "UPR Utuado", "UPR Bayamón"]
        return context
