from django.urls import path
from basicapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("formpage/", views.form_name_view, name="formpage"),
]
