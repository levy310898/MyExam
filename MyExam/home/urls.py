from django.urls import path
from . import views
urlpatterns = [
    path('', views.signIn, name = 'sign in'),
    path('base/',views.base, name = 'base'),
    path('home/',views.index, name = 'home'),

]
