from django.db import models
from datetime import datetime, timezone
from math import log


class Confession(models.Model):
    # Confession information
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=20)

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
    def time_since(self):
        return (datetime.now(timezone.utc) - self.created_at).total_seconds() / 60

    @property
    def hotness(self):
        ts = self.time_since
        s = self.score
        order = log(max(abs(s), 1), 10)
        sign = 1 if s > 0 else -1 if s < 0 else 0
        return round(sign * order + ts / 45000, 7)

    def __str__(self):
        return self.title + " - " + self.created_at.strftime("%m/%d/%Y, %H:%M:%S")
