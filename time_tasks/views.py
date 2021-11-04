from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    template_name = "index/index.html"
    context={
        "pgname":"Welcome to Time/Tasks!"
    }
    print(f"HOME called request {request} template {template_name} context {context}")

    return render(request,template_name,context)