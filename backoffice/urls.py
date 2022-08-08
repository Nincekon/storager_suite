from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('seekAdmin/dashboard', views.index, name="dashboard"),
    path('/orders', views.get_orders, name="orders"),
]