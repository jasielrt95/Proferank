from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = LoginForm()
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password', 'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password != password_confirm:
            form = RegisterForm()
            return render(request, 'accounts/register.html', {'error': 'Passwords do not match', 'form': form})
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('/')

    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})