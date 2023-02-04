from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timezone

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=False, blank=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )

    class Meta:
        abstract = True

    @property
    def score(self):
        return self.upvotes_count - self.downvotes_count

    @property
    def upvotes_count(self):
        return self.upvotes.count()

    @property
    def downvotes_count(self):
        return self.downvotes.count()

    @property
    def time_since(self):
        return (datetime.now(timezone.utc) - self.created_at).total_seconds() / 60

    @property
    def time_since_str(self):
        ts = self.time_since
        if ts < 1:
            return "Justo ahora"
        elif ts < 60:
            return "Hace " + str(round(ts)) + " minutos"
        elif ts < 1440:
            return "Hace " + str(round(ts / 60)) + " horas"
        elif ts < 43200:
            return "Hace " + str(round(ts / 1440)) + " días"
        elif ts < 525600:
            return "Hace " + str(round(ts / 43200)) + " meses"
        else:
            return "Hace " + str(round(ts / 525600)) + " años"

    def __str__(self):
        return self.text


class Confession_Comment(Comment):
    confession = models.ForeignKey("confessions.Confession", on_delete=models.CASCADE)
    # Score
    upvotes = models.ManyToManyField(User, related_name="confession_comment_upvotes")
    downvotes = models.ManyToManyField(
        User, related_name="confession_comment_downvotes"
    )

    def __str__(self):
        return self.text


class Course_Comment(Comment):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    # Score
    upvotes = models.ManyToManyField(User, related_name="course_comment_upvotes")
    downvotes = models.ManyToManyField(User, related_name="course_comment_downvotes")

    def __str__(self):
        return self.text
