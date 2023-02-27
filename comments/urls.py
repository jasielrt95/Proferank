from django.urls import path

from .views import (
    CourseCommentCreateView,
    CourseCommentLikeView,
    CourseCommentDislikeView,
    ConfessionCommentLikeView,
    ConfessionCommentDislikeView,
    CourseCommentUpdateView,
    ConfessionCommentCreateView,
    ConfessionCommentUpdateView,
)

app_name = "comments"

urlpatterns = [
    path(
        "course/<int:pk>/comment",
        CourseCommentCreateView.as_view(),
        name="course_comment",
    ),
    path(
        "courses/<int:pk>/like",
        CourseCommentLikeView,
        name="comment_like",
    ),
    path(
        "courses/<int:pk>/dislike",
        CourseCommentDislikeView,
        name="comment_dislike",
    ),
    path(
        "confessions/<int:pk>/like",
        ConfessionCommentLikeView,
        name="confession_comment_like",
    ),
    path(
        "confessions/<int:pk>/dislike",
        ConfessionCommentDislikeView,
        name="confession_comment_dislike",
    ),
    path(
        "course/<int:pk>/edit",
        CourseCommentUpdateView.as_view(),
        name="comment_edit",
    ),
    path(
        "confession/<int:pk>/edit",
        ConfessionCommentUpdateView.as_view(),
        name="confession_comment_edit",
    ),
    path(
        "confession/<int:pk>/comment",
        ConfessionCommentCreateView.as_view(),
        name="confession_comment",
    ),
]
