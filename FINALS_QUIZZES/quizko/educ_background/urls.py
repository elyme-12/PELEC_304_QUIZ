from django.urls import path
from . import views

urlpatterns = [
    path('elementary/', views.elementary, name = 'elementary'),
    path('highschool/', views.highschool, name = 'highschool'),
    path('seniorhigh/', views.seniorhigh, name = 'seniorhigh'),
]