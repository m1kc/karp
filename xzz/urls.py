from django.urls import path

from . import views

urlpatterns = [
    path('chain/<int:n>/', views.chain, name='chain'),
    path('selfref/', views.selfref, name='selfref'),
    path('cycle/<int:n>/', views.cycle, name='cycle'),
    path('infinite/', views.infinite, name='infinite'),
    path('normal/', views.normal, name='normal'),
]
