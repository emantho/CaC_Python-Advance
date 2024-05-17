from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello to ALBA PASTICCERIA")

def index(request):
    return render(request, 'alba_pasticceria/index.html')

