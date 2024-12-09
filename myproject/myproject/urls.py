"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from myapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path("accounts/register/", views.register_view, name="register"),
    path("protected/courses", views.courses_view, name="courses"),
    path("protected/my_courses", views.my_courses_view, name="my_courses"),
    path("protected/contacts",views.contact_view,name="contacts"),
    path("register-course/<int:course_id>/", views.register_course_view, name="register_course"),
]
