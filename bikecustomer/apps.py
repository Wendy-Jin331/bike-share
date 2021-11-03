from django.apps import AppConfig


class BikecustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bikecustomer'

class BikeoperatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bikeoperator'

