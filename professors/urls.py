from django.urls import path


from .views import ProfessorListView, ProfessorDetailView

urlpatterns = [
    path('all', ProfessorListView.as_view()),
    path('<int:pk>', ProfessorDetailView.as_view(), name='specific_professor'),
]