from django.urls import path
from bikecustomer import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    #path('', views.login, name='login'),
    path('', views.home, name='Home page'),
    path('hirebike/', views.hirebike, name='Hire a Bike'),
    path('logout/', views.logout, name='Log Out'),
    path('', views.base, name='Base'),
    path('hiresession/', views.hiresession, name='Hiresession'),
]



