from django.db import models

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

