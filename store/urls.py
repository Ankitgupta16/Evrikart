
from django.contrib import admin
from django.urls import path
from . import views
from django.urls.conf import include

urlpatterns = [
    path('',views.UrstoreList.as_view(), name='Urstore-list'),
    path('<str:pk>/', views.UrstoreView.as_view(), name='Urstore-detail'),

]