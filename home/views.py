from django.views.generic import TemplateView

# import the comment model
from confessions.models import Confession


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
