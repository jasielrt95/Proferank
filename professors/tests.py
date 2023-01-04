from django.test import TestCase
from professors.models import Professor


class ProfessorModelTest(TestCase):
    def setUp(self) -> None:
        Professor.objects.create(
            first_name="John",
            last_name="Doe",
            college="UPRRP",
            faculty="Naturales",
            pro_student=True,
            organized=True,
            score=0,
            total_reviews=0,
        )

    def test_getCollege(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(professor.getCollege(), "UPRRP")

    def test_getFaculty(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(professor.getFaculty(), "Naturales")

    def test_getFirstName(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(professor.getFirstName(), "John")

    def test_getLastName(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(professor.getLastName(), "Doe")

    def test_addScore(self):
        professor = Professor.objects.get(id=1)
        professor.__setattr__("score", 4)
        professor.__setattr__("total_reviews", 1)
        self.assertEqual(professor.getScore(), 4)
        self.assertEqual(professor.getTotalReviews(), 1)
        self.assertEqual(professor.avg_score, "A")

    def test_getIsProfProStudent(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(professor.getIsProfProStudent(), True)

    def test_getIsProfOrganized(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(professor.getIsProfOrganized(), True)

    def test_getScore(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(professor.getScore(), 0)

    def test_getTotalReviews(self):
        professor = Professor.objects.get(id=1)
        self.assertEqual(professor.getTotalReviews(), 0)
