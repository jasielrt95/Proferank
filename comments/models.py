from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=False)

    # Score
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def score(self):
        return self.upvotes - self.downvotes
    
    def __str__(self):
        return self.text