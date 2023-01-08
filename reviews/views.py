from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Review
from courses.models import Course
from professors.models import Professor
from .forms import ReviewForm
from django.views.generic.edit import FormView


class ReviewFormView(FormView):
    template_name = "rate_professor.html"
    form_class = ReviewForm
    success_url = "/"

    def form_valid(self, form):
        user = self.request.user
        course = Course.objects.get(pk=self.kwargs["pk"])
        # get the professor from the course
        professor = Professor.objects.get(pk=course.professor.pk)

        form.save(user=user, course=course, professor=professor)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context
