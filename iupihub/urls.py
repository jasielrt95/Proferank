"""iupihub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    path("", include("home.urls"), name="home"),
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path(
        "professors/",
        include(("professors.urls", "professors"), namespace="professors"),
    ),
    path("courses/", include(("courses.urls", "courses"), namespace="courses")),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path("reviews/", include(("reviews.urls", "reviews"), namespace="reviews")),
    path("comments/", include(("comments.urls", "comments"), namespace="comments")),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path(
        "confessions/",
        include(("confessions.urls", "confessions"), namespace="confessions"),
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
