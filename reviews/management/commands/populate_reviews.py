from django.core.management.base import BaseCommand
from faker import Faker

from reviews.models import Review
from professors.models import Professor
from courses.models import Course
from accounts.models import User

import random


class Command(BaseCommand):
    help = "Populates the database with reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            help="Indicates the number of reviews to be created",
        )

    def handle(self, *args, **options):
        fake = Faker()
        Professors = Professor.objects.all()
        user = fake.random_element(elements=User.objects.all())
        for professor in Professors:
            courses = Course.objects.filter(professor=professor)
            for course in courses:
                for i in range(1, 5):
                    Review.objects.create(
                        professor=professor,
                        course=course,
                        user=user,
                        difficulty=random.choice(["A", "B", "C", "D", "F"]),
                        grade=random.choice(["A", "B", "C", "D", "F"]),
                        recommended=fake.boolean(),
                        organized=fake.boolean(),
                    )
        self.stdout.write(self.style.SUCCESS("Successfully populated reviews!"))
