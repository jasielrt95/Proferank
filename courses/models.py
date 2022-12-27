from django.db import models


class Course(models.Model):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"
    DIFFICULTIES = ((A, "A"), (B, "B"), (C, "C"), (D, "D"), (F, "F"))


    professor = models.ForeignKey("professors.Professor", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    codification = models.CharField(max_length=8)
    difficulty = models.CharField(choices=DIFFICULTIES, max_length=1)
    average_difficulty = models.CharField(choices=DIFFICULTIES, max_length=1)
    average_grade = models.CharField(choices=DIFFICULTIES, max_length=1)
    pro_student = models.BooleanField()
    organized = models.BooleanField()

    def __str__(self):
        return self.codification
    