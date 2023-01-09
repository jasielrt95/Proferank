from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Review(models.Model):

    # Constants
    DIFFICULTIES = (
        ("A", "Very Easy"),
        ("B", "Easy"),
        ("C", "Average"),
        ("D", "Hard"),
        ("F", "Very Hard"),
    )
    GRADES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("F", "F"),
    )
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
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTIES,
    )

    grade = models.CharField(
        max_length=1,
        choices=GRADES,
    )

    pro_student = models.BooleanField()
    organized = models.BooleanField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Methods
    def letter_to_num(self, letter):
        if letter == "A":
            return 4
        elif letter == "B":
            return 3
        elif letter == "C":
            return 2
        elif letter == "D":
            return 1
        elif letter == "F":
            return 0

    @property
    def grade_num(self):
        return self.letter_to_num(self.grade)

    @property
    def difficulty_num(self):
        return self.letter_to_num(self.difficulty)

    def __str__(self):
        return f"{self.user} - {self.professor} - {self.course}"
