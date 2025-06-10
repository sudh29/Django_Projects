from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, this is the home page!")
    return render(request, "myapp/home.html")
