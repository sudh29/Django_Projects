from django.shortcuts import render
from firstapp.models import AcessRecord

# Create your views here.


def index(request):
    webpage_list = AcessRecord.objects.order_by("date")
    date_dict = {"access_records": webpage_list}
    # my_dict = {'insert_me': 'Hello I am from views.py'}
    # return HttpResponse("Hello World!")
    return render(request, "firstapp/index.html", context=date_dict)
