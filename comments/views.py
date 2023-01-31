from django.views.generic import CreateView, View
from .models import Course_Comment
from courses.models import Course
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


class CourseCommentCreateView(CreateView, LoginRequiredMixin):
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
    

# like and dislike views
def CommentLikeView(request, pk):
    comment = Course_Comment.objects.get(id=pk)
    liked = False
    if comment.upvotes.filter(id=request.user.id).exists():
        comment.upvotes.remove(request.user)
        liked = False
    else:
        comment.upvotes.add(request.user)
        liked = True
    like_count = comment.upvotes.count()
    return JsonResponse({"likecount": like_count})