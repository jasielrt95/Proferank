from django.core.management.base import BaseCommand
from faker import Faker
import random

from comments.models import Confession_Comment
from confessions.models import Confession
from accounts.models import User

class Command(BaseCommand):
    help = "Populates the database with course comments"

    def handle(self, *args, **options):
        confessions = Confession.objects.all()
        users = User.objects.all()
        fake = Faker()
        for confession in confessions:
            for i in range(random.randint(1, 10)):
                Confession_Comment.objects.create(
                    user=random.choice(users),
                    text=fake.text(max_nb_chars=200),
                    confession=confession,
                )
        self.stdout.write(self.style.SUCCESS("Successfully populated database"))