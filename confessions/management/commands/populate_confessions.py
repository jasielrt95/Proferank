from django.core.management.base import BaseCommand
from faker import Faker

from confessions.models import Confession

class Command(BaseCommand):
    help = "Populates the database with confessions"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            type=int,
            help="Indicates the number of confessions to be created",
        )

    def handle(self, *args, **options):
        fake = Faker()
        number = options.get("number")
        if number is None:
            number = 100
        for i in range(number):
            Confession.objects.create(
                title=fake.sentence(nb_words=6, variable_nb_words=True),
                body=fake.text(max_nb_chars=200),
                author=fake.name(),
            )
        self.stdout.write(self.style.SUCCESS("Successfully populated database"))
