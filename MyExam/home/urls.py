from django.urls import path
from . import views
urlpatterns = [
    path('', views.signIn, name = "signIn"),
]
