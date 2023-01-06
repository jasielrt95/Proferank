from django.core.management.base import BaseCommand
from faker import Faker
import random

from courses.models import Course
from professors.models import Professor

class Command(BaseCommand):
    help = "Populates the database with courses"

    def handle(self, *args, **options):
        professors = Professor.objects.all()
        fake = Faker()
        for professor in professors:
            for i in range(random.randint(1, 5)):
                Course.objects.create(
                    name=fake.sentence(nb_words=6, variable_nb_words=True),
                    codification=fake.random_element(elements=("CSCI", "MATH", "PHYS", "CHEM", "BIO", "ECON", "PSYC", "HIST", "ENGL", "SPAN", "FREN", "GERM", "ITAL", "CHIN", "JAPN", "ARAB", "RUSS", "LATN", "GREE", "HEBR", "PHIL", "MUSC", "ARTS", "THEA", "DANC", "COMM", "POLI", "SOCI", "ANTH", "EDUC", "LAW", "BUSI", "MKTG", "FINA", "ACCT", "ECON", "ENGR", "CIVL", "ELEC", "MECH", "ARCH", "BIOM", "CHEM", "CSCI", "ENGR", "MATH", "PHYS", "PSYC", "SOCI", "ANTH", "EDUC", "LAW", "BUSI", "MKTG", "FINA", "ACCT", "ECON", "ENGR", "CIVL", "ELEC", "MECH", "ARCH", "BIOM", "CHEM", "CSCI", "ENGR", "MATH", "PHYS", "PSYC", "SOCI", "ANTH", "EDUC", "LAW", "BUSI", "MKTG", "FINA", "ACCT", "ECON", "ENGR", "CIVL", "ELEC", "MECH", "ARCH", "BIOM", "CHEM", "CSCI", "ENGR", "MATH", "PHYS", "PSYC", "SOCI", "ANTH", "EDUC", "LAW", "BUSI", "MKTG", "FINA", "ACCT", "ECON", "ENGR", "CIVL", "ELEC", "MECH", "ARCH", "BIOM", "CHEM", "CSCI", "ENGR", "MATH", "PHYS", "PSYC", "SOCI", "ANTH", "EDUC", "LAW", "BUSI", "MKTG", "FINA", "ACCT", "ECON", "ENGR", "CIVL", "ELEC")),
                    professor=professor,
                )
        self.stdout.write(self.style.SUCCESS("Successfully populated database"))