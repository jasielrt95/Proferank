from django.db import models
from courses.models import Course
from reviews.models import Review


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
    FACULTIES = ((Natu, "Naturales"), (Huma, "Humanidades"))

    # Colleges
    UPRRP = "UPRRP"
    UPRM = "UPRM"
    COLLEGES = ((UPRRP, "UPRRP"), (UPRM, "UPRM"))

    # Professor information
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=80)
    college = models.CharField(choices=COLLEGES, max_length=100)
    faculty = models.CharField(choices=FACULTIES, max_length=30)

    @property
    def average_score(self):
        courses = Course.objects.filter(professor=self)
        reviews = Review.objects.filter(course__in=courses)
        if reviews.count() == 0:
            return 0
        return sum([review.score for review in reviews]) / reviews.count()

    @property
    def average_difficulty(self):
        courses = Course.objects.filter(professor=self)
        reviews = Review.objects.filter(course__in=courses)
        if reviews.count() == 0:
            return 0
        return self.num_to_letter(sum([review.difficulty for review in reviews]) / reviews.count())

    @property
    def average_grade(self):
        courses = Course.objects.filter(professor=self)
        reviews = Review.objects.filter(course__in=courses)
        if reviews.count() == 0:
            return 0
        return self.num_to_letter(sum([review.grade for review in reviews]) / reviews.count())

    @property
    def average_pro_student(self):
        courses = Course.objects.filter(professor=self)
        reviews = Review.objects.filter(course__in=courses)
        if reviews.count() == 0:
            return "No"
        true = reviews.filter(pro_student=True).count()
        false = reviews.filter(pro_student=False).count()
        if true > false:
            return "Yes"
        else:
            return "No"


    @property
    def average_organized(self):
        courses = Course.objects.filter(professor=self)
        reviews = Review.objects.filter(course__in=courses)
        if reviews.count() == 0:
            return "No"
        true = reviews.filter(organized=True).count()
        false = reviews.filter(organized=False).count()
        if true > false:
            return "Yes"
        else:
            return "No"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def num_to_letter(self, num):
        if num >= 3.7:
            return "A"
        elif num >= 3:
            return "B"
        elif num >= 1.7:
            return "C"
        elif num >= 1:
            return "D"
        else:
            return "F"


            
    class Meta:
        ordering = ["last_name", "first_name"]
