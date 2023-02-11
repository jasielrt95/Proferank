from django.views.generic import ListView, DetailView, CreateView
from .models import Professor, College, Department
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
    fields = ["first_name", "last_name"]
    success_url = reverse_lazy("professors:all_professors")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get all the departments objects
        departments = Department.objects.all()
        universities = College.objects.all()
        context["universities"] = universities
        context["departments"] = departments
        return context

    # adds the department and college to the professor object
    def form_valid(self, form):
        if self.request.POST["college"] == "Other":
            # get or create a new college
            new_college, created = College.objects.get_or_create(
                name=self.request.POST["other_college"]
            )
            form.instance.college = new_college
        else:
            form.instance.college = College.objects.get(pk=self.request.POST["college"])

        if self.request.POST["department"] == "Other":
            # get or create a new department
            new_department, created = Department.objects.get_or_create(
                name=self.request.POST["other_department"]
            )
            form.instance.department = new_department
        else:
            form.instance.department = Department.objects.get(
                pk=self.request.POST["department"]
            )
        return super().form_valid(form)
