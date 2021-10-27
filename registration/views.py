from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

import djangoProject.settings
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.views import generic


# ----------------index----------------
def index(request):
    return render(request, 'registration/index.html', {'title': 'index'})


# ----------------register here----------------
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # mail system
            htmly = get_template('registration/Email.html')
            d = {'username': username}
            subject, from_email, to = 'Please confirm your email', djangoProject.settings.EMAIL_HOST_USER, email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('userReg:login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form, 'title': 'reqister here'})


# ----------------login forms----------------
def user_login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('userReg:index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form, 'title': 'log in'})
