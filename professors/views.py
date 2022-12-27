from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Professor

class ProfessorListView(ListView):
    model = Professor
    template_name = "ProfessorList.html"
    

# Create your views here.
