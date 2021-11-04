from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.utils.http import is_safe_url
from django.urls import reverse
from django.utils.safestring import mark_safe

# Login/related authentication parameters
from django.contrib.auth import authenticate, login, logout, get_user_model

# Mixins
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Views
from django.views.generic.edit import FormMixin
from django.views.generic import (
    View,
    FormView,
    UpdateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)

# Flash messages
from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test,
)
from django.contrib.auth.models import Group


# Create your views here.
class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'apps/accounts/home.html'

    def get_object(self):
        return self.request.user



def login_view(request, *args, **kwargs):
    template_name="apps/accounts/forms/auth.html"
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Login",
        "title": "Login"
    }
    return render(request,template_name,context)

def logout_view(request, *args, **kwargs):
    template_name="apps/account/forms/auth.html"
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    context = {
        "form": None,
        "description": "Are you sure you want to logout?",
        "btn_label": "Click to Confirm",
        "title": "Logout"
    }
    return render(request,template_name, context)


def register_view(request, *args, **kwargs):
    template_name="apps/account/forms/auth.html"
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        # send a confirmation email to verify their account
        login(request, user)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Register",
        "title": "Register"
    }
    return render(request,template_name, context)