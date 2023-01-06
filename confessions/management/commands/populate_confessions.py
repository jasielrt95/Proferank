from django.core.management.base import BaseCommand
from faker import Faker

from confessions.models import Confession

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        for i in range(100):
            Confession.objects.create(
                title=fake.sentence(nb_words=6, variable_nb_words=True),
                body=fake.text(max_nb_chars=200),
                author=fake.name(),
            )
        self.stdout.write(self.style.SUCCESS("Successfully populated database"))
