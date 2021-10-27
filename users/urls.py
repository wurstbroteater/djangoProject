from django.conf.urls import include, url
from users.views import dashboard

urlpatterns = [
    url("accounts/", include("django.contrib.auth.urls")),
    url("dashboard/", dashboard, name="dashboard"),
]
