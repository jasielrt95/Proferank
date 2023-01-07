from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Review(models.Model):

    # Foreign keys
    professor = models.ForeignKey(
        "professors.Professor", on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="reviews"
    )
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="reviews"
    )

    # Grading
    difficulty = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
    pro_student = models.BooleanField()
    organized = models.BooleanField()

    # Score information
    score = models.IntegerField(default=0)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            self.professor.getFirstName()
            + " "
            + self.professor.getLastName()
            + " "
            + self.course.codification
            + " "
            + self.user.username
        )
