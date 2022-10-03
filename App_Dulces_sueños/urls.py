import imp
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from App_Dulces_sueños import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('categoria/', views.CategoriaView.as_view()),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view()),

    path('modelo/', views.ModeloView.as_view()),
    path('modelo/<int:pk>/', views.ModeloDetailView.as_view()),

    path('producto/', views.ProductoView.as_view()),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view()),

    path('clientes/', views.ClientesView.as_view()),
    path('clientes/<int:pk>/', views.ClientesDetailView.as_view()),


]
