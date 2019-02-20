from django.urls import path
from . import views

urlpatterns = [
    path('', views.taste_list, name='taste_list'),
    path('taste/<int:pk>/', views.taste_detail, name='taste_detail'),
]
