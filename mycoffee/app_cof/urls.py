from django.urls import path
from . import views

urlpatterns = [
    path('coffees/', views.coffees, name='coffees'),
    path('<int:coffee_id>/', views.coffee, name='coffee'),
]
