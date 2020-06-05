from django.urls import path
from . import views
urlpatterns = [
    path('sign-in/', views.signIn, name = "signIn"),
    path('index/', views.index, name= "Index"),
    path('sign-up/', views.signUp, name= "signUp"),
]
