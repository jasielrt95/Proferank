from django.core.management.base import BaseCommand
from faker import Faker
import random

from comments.models import Course_Comment
from courses.models import Course
from accounts.models import User

class Command(BaseCommand):
    help = "Populates the database with course comments"

    def handle(self, *args, **options):
        courses = Course.objects.all()
        users = User.objects.all()
        fake = Faker()
        for course in courses:
            for i in range(random.randint(1, 10)):
                Course_Comment.objects.create(
                    user=random.choice(users),
                    text=fake.text(max_nb_chars=200),
                    course=course,
                )
        self.stdout.write(self.style.SUCCESS("Successfully populated database"))