from django.urls import path
from bikeoperator import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
path('loginop/', views.loginop, name='login'),
path('homeop/', views.homeop, name='Home page'),
path('track/', views.track, name='Track a Bike'),
path('repair/', views.repair, name='Repair a Bike'),
path('move/', views.move, name='Move a Bike'),
]