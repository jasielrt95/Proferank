from django.core.management.base import BaseCommand
from faker import Faker

from professors.models import Professor


class Command(BaseCommand):
    help = "Populates the database with professors"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            help="Indicates the number of professors to be created",
        )

    def handle(self, *args, **options):
        fake = Faker()
        number = options.get("number")
        if number is None:
            number = 100
        for i in range(number):
            Professor.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                college=fake.random_element(elements=("UPRRP", "UPRM")),
                faculty=fake.random_element(elements=("Naturales", "Humanidades")),
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated database"))
