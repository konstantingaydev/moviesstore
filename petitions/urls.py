from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='petitions.index'),
    path('create/', views.create, name='petitions.create'),
    path('upvote/<int:id>/', views.upvote, name='petitions.upvote'),
]