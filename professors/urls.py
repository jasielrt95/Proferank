from django.urls import path


from .views import ProfessorListView, ProfessorDetailView, ProfessorCreateView

app_name = "professors"

urlpatterns = [
    path("all", ProfessorListView.as_view(), name="all_professors"),
    path("<int:pk>", ProfessorDetailView.as_view(), name="specific_professor"),
    path("create", ProfessorCreateView.as_view(), name="create_professor"),
]
