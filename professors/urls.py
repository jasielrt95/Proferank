from django.urls import path


from .views import ProfessorListView

urlpatterns = [
    path('', ProfessorListView.as_view()),
]