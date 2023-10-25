from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('produk/', views.produk, name='produk'),
]