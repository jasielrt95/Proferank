from django.contrib import admin

# Register your models here.
from .models import Professor


class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "college",
        "department",
        "difficulty",
        "grade",
        "pro_student",
        "organized",
        "comment_count",
    )
    list_filter = ("college", "department")
    search_fields = ("first_name", "last_name", "college", "department")


admin.site.register(Professor, ProfessorAdmin)
