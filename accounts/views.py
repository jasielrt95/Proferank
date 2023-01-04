from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})