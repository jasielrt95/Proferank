from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Confession
from comments.models import Confession_Comment
from professors.models import College
from datetime import datetime, timezone, timedelta


class ConfessionFeedView(TemplateView):
    template_name = "confession_feed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.request.GET.get("order")
        # TODO: This whole function code is very messy, I need to clean it up, divide it into functions, etc.
        try:
            college = self.request.GET.get("college")
        except:
            college = None
        if college == "all":
            college = None

        if order == "hot":
            # TODO: This method is not efficient, but it works for now, if theres a lot of posts in the last 5 days it will have to order all of them, which is not ideal.

            # get all confessions from the last 5 days
            now = datetime.now(timezone.utc)
            if college is None:
                confessions = Confession.objects.filter(
                    created_at__gte=now - timedelta(days=1)
                )
            else:
                confessions = Confession.objects.filter(
                    created_at__gte=now - timezone.timedelta(days=5), college=college
                )
            confessions = sorted(confessions, key=lambda x: x.hotness, reverse=True)
        else:
            if college is None:
                confessions = Confession.objects.all().order_by("-created_at")
            else:
                confessions = Confession.objects.filter(college=college).order_by(
                    "-created_at"
                )

        paginator = Paginator(confessions, 8)
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


class ConfessionDetailView(DetailView):
    model = Confession
    template_name = "confession_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Confession_Comment.objects.filter(
            confession=self.object
        ).order_by("created_at")
        return context
