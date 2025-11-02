from django.contrib import admin
from django.urls import path
from home import views

# Admin Header

admin.site.site_header = "Developer Sudhanshu"
admin.site.site_title = "Welcome to Sudhanshu's Dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("contact", views.contact, name="contact"),
]
