from django.urls import path
from . import views

urlpatterns = [
    path('', views.taste_list, name='taste_list'),
    path('taste/<int:pk>/', views.taste_detail, name='taste_detail'),
    path('taste/new/', views.taste_new, name='taste_new'),
    path('taste/<int:pk>/edit/', views.taste_edit, name='taste_edit'),
]
