from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Confession
from comments.models import Confession_Comment
from professors.models import College
from datetime import datetime, timezone


class ConfessionFeedView(TemplateView):
    template_name = "confession_feed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.request.GET.get("order")
        if order == "hot":
            # get all confessions from the last 5 days
            now = datetime.now(timezone.utc)
            confessions = Confession.objects.filter(
                created_at__gte=now - timezone.timedelta(days=5)
            )
            confessions = sorted(confessions, key=lambda x: x.hotness, reverse=True)
        else:
            confessions = Confession.objects.all().order_by("-created_at")
        paginator = Paginator(confessions, 50)
        page = self.request.GET.get("page")
        try:
            confessions = paginator.page(page)
            paginator.adjusted_elided_pages = paginator.get_elided_page_range(
                page, on_each_side=2, on_ends=1
            )
        except PageNotAnInteger:
            confessions = paginator.page(1)
            paginator.adjusted_elided_pages = paginator.get_elided_page_range(1)
        except EmptyPage:
            confessions = paginator.page(paginator.num_pages)
            paginator.adjusted_elided_pages = paginator.get_elided_page_range(
                paginator.num_pages
            )

        context["confessions"] = confessions
        context["paginator"] = paginator
        context["universities"] = College.objects.all()
        return context
