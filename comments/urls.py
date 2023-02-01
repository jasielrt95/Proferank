from django.urls import path

from .views import CourseCommentCreateView, CommentLikeView, CommentDislikeView

app_name = "comments"

urlpatterns = [
    path(
        "course/<int:pk>/comment",
        CourseCommentCreateView.as_view(),
        name="course_comment",
    ),
    path(
        "<int:pk>/like",
        CommentLikeView,
        name="comment_like",
    ),
    path(
        "<int:pk>/dislike",
        CommentDislikeView,
        name="comment_dislike",
    ),
]
