from django.conf.urls import include, url
from django.urls import path
from users.views import dashboard, register

urlpatterns = [
    # url("", dashboard),
    # path("accounts/", include('django_registration.backends.activation.urls')),
    url("accounts/", include("django.contrib.auth.urls")),
    url("dashboard/", dashboard, name="dashboard"),
    url("register/", register, name="register"),
]
