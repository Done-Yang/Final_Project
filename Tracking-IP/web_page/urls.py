from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('about/', views.aboutpage, name="about"),
    path('search/', views.search_result, name="search"),
]
