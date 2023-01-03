from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=False)

    # Score
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

    @property
    def score(self):
        return self.upvotes - self.downvotes
    
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

class Reply_Comment(Comment):
    comment = models.ForeignKey("comments.Confession_Comment", on_delete=models.CASCADE)

    def __str__(self):
        return self.text