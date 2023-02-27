from .models import Review, Suggestions
from courses.models import Course
from professors.models import Professor
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class ReviewFormView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "course_review.html"
    fields = ["difficulty", "grade", "recommended", "organized"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.course = Course.objects.get(id=self.kwargs["pk"])
        form.instance.professor = form.instance.course.professor
        form.save()
        return redirect("courses:specific_course", pk=self.kwargs["pk"])


class UpdateReviewFormView(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = "course_review.html"
    fields = ["difficulty", "grade", "recommended", "organized"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.course = Course.objects.get(id=self.kwargs["pk"])
        form.instance.professor = form.instance.course.professor
        form.save()
        return redirect("courses:specific_course", pk=self.kwargs["pk"])


class SuggestionsFormView(LoginRequiredMixin, CreateView):
    model = Suggestions
    template_name = "suggestions.html"
    fields = ["suggestion"]
    redirect_field_name = "next"

    def form_valid(self, form):
        form.instance.user = self.request.user
        next = self.request.GET.get("next")
        if not next:
            next = self.request.POST.get("next")
        if not next:
            next = "/"
        form.save()
        return redirect(next)
