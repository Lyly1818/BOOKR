from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = "Tina"
    return render(request, "base.html", {"name": name})
