from django.urls import path

from . import views as reg_view
from django.contrib.auth import views as auth

app_name = 'userReg'
urlpatterns = [
    path('', reg_view.index, name='index'),
    path('login/', reg_view.user_login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='registration/index.html'), name='logout'),
    path('register/', reg_view.register, name='register'),
]
