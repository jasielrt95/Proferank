from django.contrib import admin
from .models import Confession


class ConfessionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "score",
        "upvotes_count",
        "downvotes_count",
        "created_at",
        "updated_at",
        "hotness",
        "time_since",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("title", "body", "author")


admin.site.register(Confession, ConfessionAdmin)
