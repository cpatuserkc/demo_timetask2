from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    template_name = "accounts/home.html"
    return render(request,template_name)