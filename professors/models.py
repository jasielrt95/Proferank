from django.db import models
from courses.models import Course
from reviews.models import Review
from django.core.validators import MinLengthValidator, MaxLengthValidator


class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Department(models.Model):
    name = models.CharField(max_length=30, validators=[MaxLengthValidator(30)])

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Professor(models.Model):
    # Grades
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"
    DIFFICULTIES = ((A, "A"), (B, "B"), (C, "C"), (D, "D"), (F, "F"))

    # Professor information
    first_name = models.CharField(
        max_length=20, validators=[MinLengthValidator(1), MaxLengthValidator(20)]
    )
    last_name = models.CharField(
        max_length=80, validators=[MinLengthValidator(1), MaxLengthValidator(80)]
    )
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    # Methods
    @property
    def difficulty(self):
        courses = Course.objects.filter(professor=self)
        if len(courses) == 0:
            return "N/A"
        total = 0
        course_count = 0
        for course in courses:
            if course.difficulty == "N/A":
                continue
            total += course.difficulty
            course_count += 1
        if course_count == 0:
            return "N/A"
        return self.num_to_letter(total / course_count)

    @property
    def grade(self):
        courses = Course.objects.filter(professor=self)
        if len(courses) == 0:
            return 0
        total = 0
        course_count = 0
        for course in courses:
            if course.grade == "N/A":
                continue
            total += course.grade
            course_count += 1
        if course_count == 0:
            return "N/A"
        return self.num_to_letter(total / course_count)

    def pro_student(self):
        courses = Course.objects.filter(professor=self)
        total = 0
        if len(courses) == 0:
            return 0
        for course in courses:
            if course.pro_student == "N/A":
                continue
            if course.pro_student:
                total += 1
            else:
                total -= 1
        return "Sí" if total > 0 else "No"

    def organized(self):
        courses = Course.objects.filter(professor=self)
        total = 0
        if len(courses) == 0:
            return 0
        for course in courses:
            if course.organized == "N/A":
                continue
            if course.organized:
                total += 1
            else:
                total -= 1
        return "Sí" if total > 0 else "No"

    @property
    def comment_count(self):
        courses = Course.objects.filter(professor=self)
        reviews = Review.objects.filter(course__in=courses)
        return reviews.count()

    @property
    def review_count(self):
        courses = Course.objects.filter(professor=self)
        reviews = Review.objects.filter(course__in=courses)
        return reviews.count()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def num_to_letter(self, num):
        if num >= 3.2:
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

    class Meta:
        ordering = ["last_name", "first_name"]
