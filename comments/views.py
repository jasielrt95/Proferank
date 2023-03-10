from django.views.generic import CreateView, UpdateView
from .models import Course_Comment, Confession_Comment
from courses.models import Course
from confessions.models import Confession
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


class CourseCommentCreateView(LoginRequiredMixin, CreateView):
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


class CourseCommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Course_Comment
    fields = ["text"]

    def form_valid(self, form):
        course_id = self.object.course.id
        form.save()
        return redirect(reverse("courses:specific_course", args=[course_id]))

    def form_invalid(self, form):
        course_id = self.object.course.id
        return redirect(reverse("courses:specific_course", args=[course_id]))


class ConfessionCommentCreateView(LoginRequiredMixin, CreateView):
    model = Confession_Comment
    fields = ["text", "confession", "anonymous"]

    def form_valid(self, form):
        confession_id = self.kwargs["pk"]
        form.instance.user = self.request.user
        form.instance.confession = Confession.objects.get(pk=confession_id)
        form.save()
        return redirect(reverse("confessions:confession_detail", args=[confession_id]))

    def form_invalid(self, form):
        confession_id = self.kwargs["pk"]
        return redirect(reverse("confessions:confession_detail", args=[confession_id]))


class ConfessionCommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Confession_Comment
    fields = ["text"]

    def form_valid(self, form):
        confession_id = self.object.confession.id
        form.save()
        return redirect(reverse("confessions:confession_detail", args=[confession_id]))

    def form_invalid(self, form):
        confession_id = self.object.confession.id
        return redirect(reverse("confessions:confession_detail", args=[confession_id]))


@login_required
def CourseCommentLikeView(request, pk):
    comment = Course_Comment.objects.get(id=pk)
    if comment.upvotes.filter(id=request.user.id).exists():
        comment.upvotes.remove(request.user)
    else:
        if comment.downvotes.filter(id=request.user.id).exists():
            comment.downvotes.remove(request.user)
        comment.upvotes.add(request.user)
    score = comment.score
    return JsonResponse({"score": score})


@login_required
def ConfessionCommentLikeView(request, pk):
    comment = Confession_Comment.objects.get(id=pk)
    if comment.upvotes.filter(id=request.user.id).exists():
        comment.upvotes.remove(request.user)
    else:
        if comment.downvotes.filter(id=request.user.id).exists():
            comment.downvotes.remove(request.user)
        comment.upvotes.add(request.user)
    score = comment.score
    return JsonResponse({"score": score})


@login_required
def CourseCommentDislikeView(request, pk):
    comment = Course_Comment.objects.get(id=pk)
    if comment.downvotes.filter(id=request.user.id).exists():
        comment.downvotes.remove(request.user)
    else:
        if comment.upvotes.filter(id=request.user.id).exists():
            comment.upvotes.remove(request.user)
        comment.downvotes.add(request.user)
    score = comment.score
    return JsonResponse({"score": score})


@login_required
def ConfessionCommentDislikeView(request, pk):
    comment = Confession_Comment.objects.get(id=pk)
    if comment.downvotes.filter(id=request.user.id).exists():
        comment.downvotes.remove(request.user)
    else:
        if comment.upvotes.filter(id=request.user.id).exists():
            comment.upvotes.remove(request.user)
        comment.downvotes.add(request.user)
    score = comment.score
    return JsonResponse({"score": score})
