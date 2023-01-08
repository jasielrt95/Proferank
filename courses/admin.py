from django.contrib import admin

# Register your models here.
from .models import Course


class courseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "codification",
        "professor",
        "difficulty",
        "grade",
        "pro_student",
        "organized",
    )
    list_filter = ("professor",)
    search_fields = ("name", "codification", "professor")


admin.site.register(Course, courseAdmin)
