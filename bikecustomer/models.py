from django.db import models

# Create your models here.

from django.utils import timezone



class Customer(models.Model):
    customer_name = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    customer_dob = models.DateField()
    customer_id = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=12)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.customer_id


class Bikeasset(models.Model):
    bike_condition = models.BooleanField()
    current_depot = models.CharField(max_length=30)
    status = models.BooleanField()
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
    bike_id = models.ForeignKey(Bikeasset,on_delete=models.CASCADE)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.session_id

    class Meta:
        verbose_name_plural = "Hire Session"

class paycred(models.Model):
    paycred_id = models.IntegerField()
    paycred_type = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.paycred_id

class Depots(models.Model):
    depot_id = models.IntegerField()
    depot_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.depot_name


class SessionPayment(models.Model):
    hiresession_id = models.IntegerField()
    payment_amount = models.IntegerField()
    payment_id = models.IntegerField()
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.depot_id
