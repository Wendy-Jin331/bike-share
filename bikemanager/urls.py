from django.urls import path
from bikemanager import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
path('login/', views.loginmg, name='Home'),
path('homemgr/', views.homemgr, name='Login'),
]