from django.contrib import admin
from .models import Review, Suggestions


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "professor",
        "course",
        "difficulty",
        "grade",
        "recommended",
        "organized",
        "grade_num",
        "difficulty_num",
    )
    list_filter = ("professor", "course")
    search_fields = ("professor", "course")


class SuggestionsAdmin(admin.ModelAdmin):
    list_display = ("user", "suggestion", "created_at", "email")
    list_filter = ("user", "created_at")
    search_fields = ("user", "suggestion")


admin.site.register(Review, ReviewAdmin)
admin.site.register(Suggestions, SuggestionsAdmin)
