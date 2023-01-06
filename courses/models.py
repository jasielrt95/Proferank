from django.db import models


class Course(models.Model):

    # Foreign keys
    professor = models.ForeignKey("professors.Professor", on_delete=models.CASCADE)

    # Course information
    name = models.CharField(max_length=100)
    codification = models.CharField(max_length=8)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codification
