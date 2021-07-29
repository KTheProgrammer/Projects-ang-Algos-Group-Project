from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('create_account', views.create_account),
    path('login', views.login),
    path('logout', views.logout),
    path('marketplace/', views.marketplace),
    path('create', views.create),
    path('<int:item_id>/delete', views.delete),
]
