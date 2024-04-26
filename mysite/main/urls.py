from django.urls import path, include
from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("send-data/", views.send_data_by_form, name="send_data"),
    path("get-data/", views.get_data_by_form, name="get_data"),
    path("django-form/", views.test_django_form, name="django_form"),
]