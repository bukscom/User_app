from django.urls import path, include

from user_auth import views

urlpatterns = [
    path('', views.index),
]
