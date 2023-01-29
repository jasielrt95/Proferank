from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timezone

User = get_user_model()

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=False, blank=False)

    # Score
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )

    class Meta:
        abstract = True

    @property
    def score(self):
        return self.upvotes - self.downvotes

    @property
    def time_since(self):
        return (datetime.now(timezone.utc) - self.created_at).total_seconds() / 60

    @property
    def time_since_str(self):
        ts = self.time_since
        if ts < 1:
            return "Just now"
        elif ts < 60:
            return str(round(ts)) + " minutes ago"
        elif ts < 1440:
            return str(round(ts / 60)) + " hours ago"
        elif ts < 43200:
            return str(round(ts / 1440)) + " days ago"
        elif ts < 525600:
            return str(round(ts / 43200)) + " months ago"
        else:
            return str(round(ts / 525600)) + " years ago"

    def __str__(self):
        return self.text


class Confession_Comment(Comment):
    confession = models.ForeignKey("confessions.Confession", on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Course_Comment(Comment):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)

    def __str__(self):
        return self.text
