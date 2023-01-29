from django.views.generic import CreateView
from .models import Course_Comment
from django.shortcuts import redirect
from django.urls import reverse


class CourseCommentCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        course_id = self.kwargs["pk"]
        comment = Course_Comment.objects.create(
            course_id=course_id,
            user=request.user,
            text=request.POST["comment"],
        )
        comment.save()
        # refresh the page
        return redirect(reverse("courses:specific_course", args=[course_id]))
    

