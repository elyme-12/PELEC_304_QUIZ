from django.urls import path
from . import views

urlpatterns = [
  path('students/', views.students, name='students'),
  path('students2/', views.students2, name='students2'),
  path('students3/', views.students3, name='students3')
]

