from django import forms
from .models import Message, Course, Profile
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "message"]

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"Name:{self.name} Email:{self.email} Message:{self.message}"


class RegisterForm(forms.ModelForm):
    """
    RegisterForm is a Django ModelForm for registering a new user.

    Attributes:
        password: A CharField representing the user's password with PasswordInput widget for obscured entry.
        password_confirm: A CharField for confirming the password, also using a PasswordInput widget.

    Meta:
        model: The User model that the form interfaces with.
        fields: Specifies which fields to include in the form - 'username', 'password', and 'password_confirm'.

    Methods:
        clean: Validates that the password and password_confirm fields match. Raises a ValidationError if they do not match.
        save: Saves the User instance with the password properly hashed if the form is valid. If commit=True, saves the instance to the database immediately.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    class Meta:
        model = User
        fields = ['username','password','password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password_confirm!=password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
