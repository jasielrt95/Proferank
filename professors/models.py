from django.db import models

# Create your models here.

class Professor(models.Model):

    # Grades
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"
    DIFFICULTIES = ((A, "A"), (B, "B"), (C, "C"), (D, "D"), (F, "F"))

    # Faculties
    Natu = "Naturales"
    Huma = "Humanidades"
    FACULTIES = ((Natu, "Naturales"), (Huma,"Humanidades"))

    # Colleges
    UPRRP = "Universidad de Puerto Rico, Rio Piedras"
    UPRM = "Universidad de Puerto Rico, Mayaguez"
    COLLEGES = ((UPRRP, "UPRRP"), (UPRM, "UPRM"))

    # Professor information
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=80)
    college = models.CharField(max_length=100, choices=COLLEGES)
    faculty = models.CharField(choices=FACULTIES, max_length=30)

    # Grading 
    average_difficulty = models.CharField(choices=DIFFICULTIES, max_length=1)
    average_grade = models.CharField(choices=DIFFICULTIES, max_length=1)
    pro_student = models.BooleanField()
    organized = models.BooleanField()

    # Score information
    score = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Getter functions for Professor class
    def getCollege(self):   
        return self.college

    def getFaculty(self):
        return self.faculty

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getAverageGrade(self):
        return self.average_grade

    def getAverageDifficulty(self):
        return self.average_difficulty

    def getIsProfProStudent(self):
        return self.pro_student

    def getIsProfOrganized(self):
        return self.organized

    def getScore(self):
        return self.score

    def getTotalReviews(self):
        return self.total_reviews

    def __str__(self):
        return self.first_name + " " + self.last_name