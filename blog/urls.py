from django.contrib import admin
from django.urls import path
from blog.views import *
urlpatterns = [
    path("", StatyaView.as_view(), name="statya"),
    path("single/<slug:slug>", SlugFilter.as_view(), name="single"),
    path("search/", SearchView.as_view(), name="search"),
]
