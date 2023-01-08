from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "professor",
        "course",
        "difficulty",
        "grade",
        "pro_student",
        "organized",
        "grade_num",
        "difficulty_num",
    )
    list_filter = ("professor", "course")
    search_fields = ("professor", "course")


admin.site.register(Review, ReviewAdmin)
