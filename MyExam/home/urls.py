from django.urls import path
from . import views
urlpatterns = [
<<<<<<< HEAD
    path('', views.signIn, name = 'sign in'),
    path('base/',views.base, name = 'base'),
    path('home/',views.index, name = 'home'),
=======
    path('sign-in/', views.signIn, name = "signIn"),
    path('index/', views.index, name= "Index"),
    path('sign-up/', views.signUp, name= "signUp"),
>>>>>>> 8d1ae608a16b788724c1b22c345bf2b4d889e946

]
