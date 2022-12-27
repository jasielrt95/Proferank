from django.db import models

# Create your models here.
class Comment(models.Model):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    # user 
    text = models.TextField(null=False)

    def __str__(self):
        return self.text