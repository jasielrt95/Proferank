from django.contrib import admin

# Register your models here.
from .models import Professor


class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "college",
        "faculty",
        "average_score",
        "average_difficulty",
        "average_grade",
        "average_pro_student",
        "average_organized",
    )
    list_filter = ("college", "faculty")
    search_fields = ("first_name", "last_name", "college", "faculty")

admin.site.register(Professor, ProfessorAdmin)
