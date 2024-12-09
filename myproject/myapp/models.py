from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Name:{self.name} Email:{self.email} Message:{self.message}"


class Course(models.Model):
    course_name = models.CharField(max_length=64)
    course_description = models.CharField(max_length=64)
    course_price = models.IntegerField()
    course_startdate = models.DateField()
    course_link = models.URLField(max_length=200, default='')

    def __str__(self):
        return f"Курс:{self.course_name} Описание:{self.course_description} Цена:{self.course_price} Начало курса:{self.course_startdate} Ссылка:{self.course_link}"


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user",
                           "course",)  # Убедитесь, что пользователь не может зарегистрироваться на один и тот же курс несколько раз.


class Profile(models.Model):
    ROLE_CHOICES = {
        "Учитель": "Учитель",
        "Ученик": "Ученик",
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='Ученик')

    def __str__(self):
        return f'Пользователь:{self.user}\n Роль:{self.role}'
