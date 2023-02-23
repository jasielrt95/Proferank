from django.db import models
from datetime import datetime, timezone
from comments.models import Confession_Comment
from math import log
from professors.models import College


class Confession(models.Model):
    # Confession information
    title = models.CharField(max_length=100)
    body = models.TextField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    # Score information
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def score(self):
        return self.upvotes - self.downvotes

    @property
    def num_comments(self):
        return Confession_Comment.objects.filter(confession=self).count()

    @property
    def time_since(self):
        return (datetime.now(timezone.utc) - self.created_at).total_seconds() / 60

    @property
    def time_since_str(self):
        ts = self.time_since
        if ts < 1:
            return "Justo ahora"
        elif ts < 60:
            return str(round(ts)) + " minutos atras"
        elif ts < 1440:
            return str(round(ts / 60)) + " horas atras"
        elif ts < 43200:
            return str(round(ts / 1440)) + " días atras"
        elif ts < 525600:
            return str(round(ts / 43200)) + " meses atras"
        else:
            return str(round(ts / 525600)) + " años atras"

    # TODO: Implement a better hotness alogorithm that scales down the score the older the post is
    @property
    def hotness(self):
        if self.time_since > 1440:
            return 0
        ts = self.time_since
        s = self.score
        order = log(max(abs(s), 1), 10)
        sign = 1 if s > 0 else -1 if s < 0 else 0
        return round(sign * order + ts / 45000, 7)

    @property
    def comment_count(self):
        return Confession_Comment.objects.filter(confession=self).count()

    def __str__(self):
        return self.title + " - " + self.created_at.strftime("%m/%d/%Y, %H:%M:%S")
