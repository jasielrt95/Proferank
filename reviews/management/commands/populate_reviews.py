from django.core.management.base import BaseCommand
from faker import Faker

from reviews.models import Review
from professors.models import Professor
from courses.models import Course
from accounts.models import User


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
        for professor in Professors:
            courses = Course.objects.filter(professor=professor)
            course = fake.random_element(elements=courses)

            user = fake.random_element(elements=User.objects.all())

            for i in range(1, 5):
                Review.objects.create(
                    professor=professor,
                    course=course,
                    user=user,
                    difficulty=fake.random_int(min=0, max=4),
                    grade=fake.random_int(min=0, max=4),
                    pro_student=fake.boolean(),
                    organized=fake.boolean(),
                    score=fake.random_int(min=0, max=4),
                )
        self.stdout.write(self.style.SUCCESS("Successfully populated database"))
