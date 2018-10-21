from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def index(request):
#    return HttpResponse("<h2>hey this is be home to the API</h2>")


def index(request):
    return render(request, 'api/home.html')