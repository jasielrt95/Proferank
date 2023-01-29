from django.db import models
from reviews.models import Review
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Course(models.Model):

    # Foreign keys
    professor = models.ForeignKey("professors.Professor", on_delete=models.CASCADE)

    # Course information
    name = models.CharField(max_length=100)
    codification = models.CharField(max_length=8, validators=[MinLengthValidator(8), MaxLengthValidator(8)])

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Methods
    @property
    def grade(self):
        reviews = Review.objects.filter(course=self)
        total = 0
        if len(reviews) == 0:
            return "N/A"
        for review in reviews:
            total += review.grade_num
        return total / len(reviews)

    @property
    def grade_letter(self):
        return self.num_to_letter(self.grade)

    @property
    def difficulty(self):
        reviews = Review.objects.filter(course=self)
        if len(reviews) == 0:
            return "N/A"
        total = 0
        for review in reviews:
            total += review.difficulty_num
        return total / len(reviews)

    @property
    def difficulty_letter(self):
        return self.num_to_letter(self.difficulty)

    @property
    def pro_student(self):
        reviews = Review.objects.filter(course=self)
        if len(reviews) == 0:
            return "N/A"
        total = 0
        for review in reviews:
            if review.pro_student:
                total += 1
            else:
                total -= 1
        return total > 0

    @property
    def pro_student_letter(self):
        return "Si" if self.pro_student else "No"

    @property
    def organized(self):
        reviews = Review.objects.filter(course=self)
        if len(reviews) == 0:
            return "N/A"
        total = 0
        for review in reviews:
            if review.organized:
                total += 1
            else:
                total -= 1
        return total > 0

    @property
    def organized_letter(self):
        return "Si" if self.organized else "No"

    @property
    def faculty(self):
        return self.professor.faculty

    @property
    def college(self):
        return self.professor.college

    def __str__(self):
        return (
            self.codification
            + " - "
            + self.professor.first_name
            + " "
            + self.professor.last_name
        )

    def num_to_letter(self, num):
        if num == "N/A":
            return "N/A"
        elif num >= 3.2:
            return "A"
        elif num >= 2.4:
            return "B"
        elif num >= 1.6:
            return "C"
        elif num >= 0.8:
            return "D"
        else:
            return "F"

    def letter_to_num(self, letter):
        if letter == "A":
            return 4
        elif letter == "B":
            return 3
        elif letter == "C":
            return 2
        elif letter == "D":
            return 1
        else:
            return 0
