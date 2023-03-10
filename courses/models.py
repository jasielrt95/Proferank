from django.db import models
from reviews.models import Review
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Course(models.Model):
    # Foreign keys
    professor = models.ForeignKey("professors.Professor", on_delete=models.CASCADE)

    # Course information
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        blank=False,
        null=False,
    )
    codification = models.CharField(
        max_length=8,
        validators=[MinLengthValidator(8), MaxLengthValidator(8)],
        blank=True,
        null=True,
    )

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
    def recommended(self):
        reviews = Review.objects.filter(course=self)
        if len(reviews) == 0:
            return "N/A"
        total = 0
        for review in reviews:
            if review.recommended:
                total += 1
            else:
                total -= 1
        return total > 0

    @property
    def recommended_letter(self):
        return "Sí" if self.recommended else "No"

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
        return "Sí" if self.organized else "No"

    @property
    def review_count(self):
        return len(Review.objects.filter(course=self))

    @property
    def department(self):
        return self.professor.department

    @property
    def college(self):
        return self.professor.college

    def __str__(self):
        if self.codification is not None:
            return self.codification
        return self.name

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
