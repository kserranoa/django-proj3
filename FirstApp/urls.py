from django.urls import path
from .views import homepageview

urlpatterns = [
    path('', homepageview.as_view()) #connect to views
]