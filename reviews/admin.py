from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "professor":
            kwargs["queryset"] = db_field.related_model.objects.filter(
                user=request.user
            )
        if db_field.name == "course":
            kwargs["queryset"] = db_field.related_model.objects.filter(
                user=request.user
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Review, ReviewAdmin)
