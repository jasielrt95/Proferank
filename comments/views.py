from django.views.generic import CreateView
from .models import Course_Comment
from courses.models import Course
from django.shortcuts import redirect
from django.urls import reverse


class CourseCommentCreateView(CreateView):
    model = Course_Comment
    fields = ["text", "course"]


    def form_valid(self, form):
        course_id = self.kwargs["pk"]
        form.instance.user = self.request.user
        form.instance.course = Course.objects.get(pk=course_id)
        form.save()
        return redirect(reverse("courses:specific_course", args=[course_id]))
    
    def form_invalid(self, form):
        course_id = self.kwargs["pk"]
        return redirect(reverse("courses:specific_course", args=[course_id]))
