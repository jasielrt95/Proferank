from django.views.generic import TemplateView, DetailView, CreateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Confession
from comments.models import Confession_Comment
from professors.models import College
from datetime import datetime, timezone, timedelta
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ConfessionFeedView(TemplateView):
    template_name = "confession_feed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            college = self.kwargs["college"]
            college = College.objects.get(name=college)
        except:
            college = None

        if college is None:
            confessions = Confession.objects.all()
        else:
            confessions = Confession.objects.filter(college=college)
            context["selected"] = college

        paginator = Paginator(confessions, 4)
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
    template_name = "confession.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Confession_Comment.objects.filter(
            confession=self.object
        ).order_by("created_at")
        return context


class ConfessionCreateView(LoginRequiredMixin, CreateView):
    model = Confession
    fields = ["title", "body"]
    template_name = "confession_create.html"

    def form_valid(self, form):
        form.instance.college = College.objects.get(id=1)
        return super().form_valid(form)

    def get_success_url(self):
        return "/confessions/" + str(self.object.id) + "/"


@login_required
def ConfessionLikeView(request, pk):
    confession = Confession.objects.get(id=pk)
    if confession.upvotes.filter(id=request.user.id).exists():
        confession.upvotes.remove(request.user)
    else:
        if confession.downvotes.filter(id=request.user.id).exists():
            confession.downvotes.remove(request.user)
        confession.upvotes.add(request.user)
    score = confession.score
    return JsonResponse({"score": score})


@login_required
def ConfessionDislikeView(request, pk):
    confession = Confession.objects.get(id=pk)
    if confession.downvotes.filter(id=request.user.id).exists():
        confession.downvotes.remove(request.user)
    else:
        if confession.upvotes.filter(id=request.user.id).exists():
            confession.upvotes.remove(request.user)
        confession.downvotes.add(request.user)
    score = confession.score
    return JsonResponse({"score": score})
