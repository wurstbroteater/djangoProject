from django.contrib import messages
from django.contrib.auth import login
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm, CustomExtendedUserCreationForm
from django.http import HttpResponse


def dashboard(request):
    return render(request, "users/dashboard.html")


@transaction.atomic
def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"user_form": CustomUserCreationForm,
             "extended_user_form": CustomExtendedUserCreationForm
             }
        )
    elif request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        user_extended_form = CustomExtendedUserCreationForm(request.POST)
        if user_form.is_valid() and user_extended_form.is_valid():
            user = user_form.save()
            user_extended = user_extended_form.save(commit=False)
            user_extended.user = user
            user_extended.save()
            login(request, user)
            messages.success(request, 'Your profile was successfully updated!')
            return redirect(reverse("dashboard"))
        else:
            return HttpResponse("Keine valide Angabe")
