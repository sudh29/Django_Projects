from django.shortcuts import render
from twoapp.models import User
from twoapp.form import NewUserForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def index(request):
    return render(request, "twoapp/index.html")


def users(request):
    user_list = User.objects.order_by("first_name")
    user_dict = {"users": user_list}
    return render(request, "twoapp/user.html", context=user_dict)


def form(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR invalid FORM")
    return render(request, "twoapp/form.html", {"form": form})
