from django.urls import path
from firstapp import views

app_name = "firstapp"

urlpatterns = [
    path("", views.index, name="index"),
]
