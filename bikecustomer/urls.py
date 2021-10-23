from django.urls import path
from bikecustomer import views
<<<<<<< HEAD
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    #path('', views.login, name='login'),
    path('', views.home, name='Home page'),
    path('hirebike/', views.hirebike, name='Hire a Bike'),
    path('logout/', views.logout, name='Log Out'),
    path('base/', views.base, name='Base'),
    path('hiresession/', views.hiresession, name='Hiresession'),
    path('', views.depots, name='deopts'),
]



=======
=======
from django.conf import settings
>>>>>>> 6d2dac84ac129412ef41d7dc46487383499d5a3e
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    #path('', views.login, name='login'),
    path('', views.home, name='Home page'),
    path('hirebike/', views.hirebike, name='Hire a Bike'),
    path('logout/', views.logout, name='Log Out'),
    path('base/', views.base, name='Base'),
    path('hiresession/', views.hiresession, name='Hiresession'),
    path('', views.depots, name='deopts'),
]



<<<<<<< HEAD
]
>>>>>>> 31d4a54... Added login Page created by Mao
=======
>>>>>>> 6d2dac84ac129412ef41d7dc46487383499d5a3e
