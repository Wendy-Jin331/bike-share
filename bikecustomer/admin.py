from django.contrib import admin

# Register your models here.
# entries/admin.py

from django.contrib import admin
from .models import Customer
from .models import Bikes
from .models import Hiresession

admin.site.register(Customer)
admin.site.register(Bikes)
admin.site.register(Hiresession)