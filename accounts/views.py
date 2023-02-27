from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from django.shortcuts import render, redirect


User = get_user_model()


class LoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    redirect_field_name = "next"

    def get_success_url(self):
        return self.get_redirect_url()

    def get_redirect_url(self) -> str:
        next = self.request.GET.get(self.redirect_field_name)
        if not next:
            next = self.request.POST.get(self.redirect_field_name)
        if not next:
            next = "/"
        return next

    # if login is not successful, return error message
    def form_invalid(self, form):
        return render(
            self.request,
            "login.html",
            {"error": "Usuario o contraseña incorrectos"},
        )


class LogoutView(LogoutView):
    template_name = "logout.html"
    redirect_field_name = "next"
    next_page = "/accounts/login/"


class RegisterView(View):
    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password != password_confirm:
            return render(
                request,
                "register.html",
                {"error": "Las contraseñas no coinciden"},
            )
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email
            )
            user.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/")

    def get(self, request):
        return render(request, "register.html")
