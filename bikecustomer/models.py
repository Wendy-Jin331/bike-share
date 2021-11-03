from django.db import models

# Create your models here.

import uuid
from django.utils import timezone
from BikeShare.settings import TIME_ZONE


class Customer(models.Model):
    customer_name = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    customer_dob = models.DateField()
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # customer_id = models.IntegerField(primary_key = True)
    customer_email = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=12)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.customer_name


class Depots(models.Model):
    depot_id = models.IntegerField(primary_key=True)
    depot_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.depot_name


class Bikeasset(models.Model):
    need_repair = models.BooleanField(default=False)
    current_depot = models.ForeignKey(Depots, on_delete=models.CASCADE, related_name='Bikeasset')
    status = models.BooleanField()
    bike_id = models.IntegerField(primary_key=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Bike assets"

    def __str__(self):
        return str(self.bike_id)


class Hiresession(models.Model):
    session_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    start_depot = models.CharField(max_length=40)
    end_depot = models.CharField(max_length=40)
    bike_id = models.ForeignKey(Bikeasset, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(default=timezone.now)
    end_date_time = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return str(self.session_id)

    class Meta:
        verbose_name_plural = "Hire Session"


class paycred(models.Model):
    paycred_id = models.IntegerField(primary_key=True)
    paycred_type = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='paycred')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.paycred_id


class SessionPayment(models.Model):
    hiresession_id = models.IntegerField()
    payment_amount = models.IntegerField()
    payment_id = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='SessionPayment')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.hiresession_id


class payment(models.Model):
    credit_card = models.IntegerField()

    def __str__(self):
        return self.credit_card
