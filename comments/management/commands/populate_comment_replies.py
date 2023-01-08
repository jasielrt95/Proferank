from django.core.management.base import BaseCommand
from faker import Faker
import random

from comments.models import Confession_Comment
from confessions.models import Confession
from accounts.models import User


class Command(BaseCommand):
    help = "Populates the database with course comments"

    def handle(self, *args, **options):
        comments = Confession_Comment.objects.all()
        users = User.objects.all()
        fake = Faker()
        for comment in comments:
            for i in range(random.randint(1, 100)):
                generate_replies = random.choice([True, False])
                comment = Confession_Comment.objects.create(
                    confession=comment.confession,
                    user=random.choice(users),
                    text=fake.text(max_nb_chars=200),
                    parent=comment,
                )
                if generate_replies:
                    for i in range(random.randint(1, 10)):
                        Confession_Comment.objects.create(
                            confession=comment.confession,
                            user=random.choice(users),
                            text=fake.text(max_nb_chars=200),
                            parent=comment,
                        )
        self.stdout.write(
            self.style.SUCCESS("Successfully populated confession comments replies!")
        )
