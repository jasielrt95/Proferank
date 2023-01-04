from django.contrib import admin

# Register your models here.
from .models import Comment, Confession_Comment, Course_Comment

admin.site.register(Confession_Comment)
admin.site.register(Course_Comment)
