from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import (
    Company
)

def home(request):
    template_name = "apps/stocks/home.html"
    pgname="Stocks"
    qs = Company.objects.all()
    context={
        "pgname":pgname,
        "object_list":qs
    }
    return render(request,template_name,context)