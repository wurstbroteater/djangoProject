from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ExtendedUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)
        model.first_name = ''
        model.last_name = ''


class CustomExtendedUserCreationForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ('institute',)
