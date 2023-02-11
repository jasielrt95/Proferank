from django.views.generic import TemplateView

# import the comment model
from confessions.models import Confession
from accounts.models import User
from comments.models import Course_Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    model = Confession
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # get all the confessions from the database
        confessions = Confession.objects.filter().order_by("-created_at")

        top_confessions = sorted(confessions, key=lambda x: x.hotness, reverse=True)[:5]

        # bottom 5 confessions
        context["confessions"] = top_confessions
        return context


class AboutView(TemplateView):
    template_name = "about.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        # get all the confessions from the database
        user = User.objects.get(username=self.request.user)
        comments = Course_Comment.objects.filter(user=user).order_by("-created_at")
        total_upvotes = 0
        total_downvotes = 0
        for comment in comments:
            total_upvotes += comment.upvotes_count
            total_downvotes += comment.downvotes_count

        context["total_upvotes"] = total_upvotes
        context["total_downvotes"] = total_downvotes
        context["comments"] = comments
        return context
