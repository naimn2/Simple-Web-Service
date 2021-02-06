from django.urls import path, include
from . import views

urlpatterns = [
    path('hero-list', views.hero_list),
    path('hero-list/<id>', views.hero_detail),
]