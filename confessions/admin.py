from django.contrib import admin
from .models import Confession


class ConfessionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "score",
        "upvotes",
        "downvotes",
        "created_at",
        "updated_at",
        "hotness",
        "time_since",
    )
    list_filter = ("author", "created_at")
    search_fields = ("title", "body", "author")


admin.site.register(Confession, ConfessionAdmin)
