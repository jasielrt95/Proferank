from django.views.generic import TemplateView

# import the comment model
from comments.models import Comment


class IndexView(TemplateView):
    template_name = "index.html"

    