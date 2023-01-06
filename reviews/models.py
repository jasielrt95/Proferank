from django.db import models


class Review(models.Model):

    # Grades
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"
    DIFFICULTIES = ((A, "A"), (B, "B"), (C, "C"), (D, "D"), (F, "F"))

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
    average_difficulty = models.CharField(choices=DIFFICULTIES, max_length=1)
    average_grade = models.CharField(choices=DIFFICULTIES, max_length=1)
    pro_student = models.BooleanField()
    organized = models.BooleanField()

    # Score information
    score = models.IntegerField(default=0)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.professor.getFirstName() + " " + self.professor.getLastName() + " " + self.course.codification + " " + self.user.username

