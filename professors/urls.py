from django.urls import path


from .views import ProfessorListView, ProfessorDetailView

app_name = "professors"

urlpatterns = [
    path("all", ProfessorListView.as_view(), name="all_professors"),
    path("<int:pk>", ProfessorDetailView.as_view(), name="specific_professor"),
]
