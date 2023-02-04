from django.views.generic import CreateView, UpdateView
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


class CourseCommentUpdateView(UpdateView, LoginRequiredMixin):
    model = Course_Comment
    fields = ["text"]

    def form_valid(self, form):
        course_id = self.object.course.id
        form.save()
        return redirect(reverse("courses:specific_course", args=[course_id]))

    def form_invalid(self, form):
        course_id = self.object.course.id
        return redirect(reverse("courses:specific_course", args=[course_id]))


def CommentLikeView(request, pk):
    comment = Course_Comment.objects.get(id=pk)
    if comment.upvotes.filter(id=request.user.id).exists():
        comment.upvotes.remove(request.user)
    else:
        if comment.downvotes.filter(id=request.user.id).exists():
            comment.downvotes.remove(request.user)
        comment.upvotes.add(request.user)
    score = comment.score
    return JsonResponse({"score": score})


def CommentDislikeView(request, pk):
    comment = Course_Comment.objects.get(id=pk)
    if comment.downvotes.filter(id=request.user.id).exists():
        comment.downvotes.remove(request.user)
    else:
        if comment.upvotes.filter(id=request.user.id).exists():
            comment.upvotes.remove(request.user)
        comment.downvotes.add(request.user)
    score = comment.score
    return JsonResponse({"score": score})
