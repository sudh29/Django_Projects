from django.urls import path
from twoapp import views

app_name = "twoapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("user/", views.users, name="users"),
    path("form/", views.form, name="form"),
]
