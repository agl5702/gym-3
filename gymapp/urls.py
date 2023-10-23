from django.contrib import admin
from django.urls import path
from gymapp import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', views.Logueo.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.app, name='app'),
    path('usuarios/', views.usuario, name='usuarios'),
    path('lector/',views.lector, name='lector'),
]
