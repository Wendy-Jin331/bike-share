from django.db import models

# Create your models here.

from django.utils import timezone


class Customer(models.Model):
    customer_name = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    customer_dob = models.DateTimeField()
    customer_id = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=30)
    customer_phone = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.customer_id


class Bikes(models.Model):
    bike_condition = models.IntegerField()
    current_depot = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    bike_id = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bike_id

    class Meta:
        verbose_name_plural = "Bike assets"


class Hiresession(models.Model):
    session_id = models.IntegerField()
    customer_id = models.CharField(max_length=100)
    start_depot = models.CharField(max_length=40)
    end_depot = models.CharField(max_length=40)
    bike_id = models.CharField(max_length=100)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.session_id

    class Meta:
        verbose_name_plural = "sessions"

class paycred(models.Model):
    session_id = models.IntegerField()
    customer_id = models.CharField(max_length=100)
    start_depot = models.CharField(max_length=40)
    end_depot = models.CharField(max_length=40)
    bike_id = models.CharField(max_length=100)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.session_id

    class Meta:
        verbose_name_plural = "sessions"