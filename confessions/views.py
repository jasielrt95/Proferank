from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Confession
from comments.models import Confession_Comment


class ConfessionFeedView(TemplateView):
    template_name = "confession_feed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.request.GET.get("order")
        if order == "hot":
            confessions = Confession.objects.all().order_by("-hotness")
            print("hot")
        else:       
            confessions = Confession.objects.all().order_by("-created_at")
        paginator = Paginator(confessions, 10)
        page = self.request.GET.get("page")
        try:
            confessions = paginator.page(page)
        except PageNotAnInteger:
            confessions = paginator.page(1)
        except EmptyPage:
            confessions = paginator.page(paginator.num_pages)
        context["confessions"] = confessions
        return context