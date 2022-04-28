from django.urls import path
from mainApp import views

urlpatterns = [
  path('', views.homehome, name="homehome"),
  path('category/', views.category, name="category")
]