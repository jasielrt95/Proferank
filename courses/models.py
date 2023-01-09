from django.db import models
from reviews.models import Review


class Course(models.Model):

    # Foreign keys
    professor = models.ForeignKey("professors.Professor", on_delete=models.CASCADE)

    # Course information
    name = models.CharField(max_length=100)
    codification = models.CharField(max_length=8)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Methods
    @property
    def grade(self):
        reviews = Review.objects.filter(course=self)
        total = 0
        if len(reviews) == 0:
            return 'N/A'
        for review in reviews:
            total += review.grade_num
        return total / len(reviews)

    @property
    def difficulty(self):
        reviews = Review.objects.filter(course=self)
        if len(reviews) == 0:
            return 'N/A'
        total = 0
        for review in reviews:
            total += review.difficulty_num
        return total / len(reviews)

    @property
    def pro_student(self):
        reviews = Review.objects.filter(course=self)
        if len(reviews) == 0:
            return 'N/A'
        total = 0
        for review in reviews:
            if review.pro_student:
                total += 1
            else:
                total -= 1
        return total > 0

    @property
    def organized(self):
        reviews = Review.objects.filter(course=self)
        if len(reviews) == 0:
            return 'N/A'
        total = 0
        for review in reviews:
            if review.organized:
                total += 1
            else:
                total -= 1
        return total > 0

    def __str__(self):
        return self.codification
