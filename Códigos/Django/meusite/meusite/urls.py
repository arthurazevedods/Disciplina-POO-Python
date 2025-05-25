from django.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls)
]

