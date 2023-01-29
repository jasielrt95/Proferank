from .models import Review
from courses.models import Course
from professors.models import Professor
from django.views.generic.edit import CreateView
from django.shortcuts import redirect


class ReviewFormView(CreateView):
    model = Review
    template_name = "course_review.html"
    fields = ["difficulty", "grade", "pro_student", "organized"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.course = Course.objects.get(id=self.kwargs["pk"])
        # get the professor from the course
        form.instance.professor = form.instance.course.professor
        form.save()
        return redirect("courses:specific_course", pk=self.kwargs["pk"])



