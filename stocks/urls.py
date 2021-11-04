from django.urls import path
from .views import home

app_name="stocks"
urlpatterns = [
    path('', home, name="home"),
]