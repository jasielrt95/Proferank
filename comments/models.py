from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    # user 
    text = models.TextField(null=False)

    # Like or Dislike options for buttons on the front-end
    like = "Like"
    dislike = "Dislike"
    forOrAgainst = ((like, "LIKE"),(dislike,"DISLKE"))

    likeOrDislike = models.CharField(choices=forOrAgainst,max_length=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text