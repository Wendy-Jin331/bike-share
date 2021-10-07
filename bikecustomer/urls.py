from django.urls import path
from bikecustomer import views

urlpatterns = [
    path('', views.login, name='login'),
]