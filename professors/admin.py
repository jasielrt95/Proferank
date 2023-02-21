from django.contrib import admin

# Register your models here.
from .models import Professor, College, Department


class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "college",
        "department",
        "difficulty",
        "grade",
        "recommended",
        "organized",
        "comment_count",
    )
    list_filter = ("college", "department")
    search_fields = ("first_name", "last_name", "college", "department")


class CollegeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Department, DepartmentAdmin)
