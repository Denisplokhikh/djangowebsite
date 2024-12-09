from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import ContactForm, RegisterForm
from .models import Course
from .models import Enrollment
# Create your views here.
def homepage(request):

    return render(request, "homepage.html")

def courses_view(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, 'registration/courses.html',context)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("contact-success")
    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "contact.html", context)


def contact_success_view(request):
    return render(request, "contact_success.html")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()  # Создайте новую форму для GET-запроса

    return render(request, "accounts/register.html", {"form": form})  # Верните форму вне условий

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = (
                request.POST.get("next") or request.GET.get("next") or "home"
            )
            return redirect(next_url)
        else:
            messages.error(request,"Invalid Login or Password!")
            return redirect('home')
    return render(request, "accounts/login.html", )


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect("home")


@login_required
def home_view(request):
    return render(request, "homepage.html")

def contact_view(request):
    return render(request,"registration/contacts.html")
def my_courses_view(request):
    enrolled_courses = Enrollment.objects.filter(user=request.user).select_related(
        "course"
    )
    context = {"enrolled_courses": enrolled_courses}
    return render(request, "registration/my_courses.html", context)
def register_course_view(request,course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        messages.success(request, "Вы успешно записались на курс!")
    else:
        messages.warning(request, "Вы уже зарегистрированы на этот курс.")

    return redirect('courses')  # Перенаправление на страницу курсов
    

# Protected View

class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # next - to redirect URL
    redirect_field_name = 'redirect_to'
    def get(self,request):
        return render(request, 'registration/protected.html')
