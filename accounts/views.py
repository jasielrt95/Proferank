from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from django.shortcuts import render, redirect


User = get_user_model()


class LoginView(LoginView):
    template_name = "accounts/login.html"
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


class LogoutView(LogoutView):
    template_name = "accounts/logout.html"
    redirect_field_name = "next"
    next_page = "/accounts/login/"


class RegisterView(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password != password_confirm:
            return render(
                request,
                "accounts/register.html",
                {"error": "Passwords do not match"},
            )
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect("/")

    def get(self, request):
        return render(request, "accounts/register.html")
