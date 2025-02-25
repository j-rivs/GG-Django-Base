from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# create a function
def gg_view(request):

    return HttpResponse("<h1>Welcome to GG</h1>")