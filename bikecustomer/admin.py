from django.contrib import admin

# Register your models here.
# entries/admin.py

from django.contrib import admin
from .models import Customer
from .models import Bikeasset
from .models import paycred
from .models import Depots
from .models import SessionPayment
from .models import Hiresession

admin.site.register(Customer)
admin.site.register(Bikeasset)
admin.site.register(Hiresession)
admin.site.register(paycred)
admin.site.register(Depots)
admin.site.register(SessionPayment)
