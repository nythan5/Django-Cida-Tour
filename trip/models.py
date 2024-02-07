from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Trip(models.Model):
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)  # noqa
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=False)
    cost = models.FloatField(default=0.00)
    price = models.FloatField(default=0.00)
    check_in_date = models.DateTimeField(null=False)
    check_out_date = models.DateTimeField(null=False)
    city = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    available_vacancies = models.IntegerField(default=0)
    cover = models.ImageField(null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    birth_date = models.DateField(null=False)
    GENDER_CHOICES = ('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.IntegerField(null=False)
    rg = models.CharField(max_length=15, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_dependency = models.BooleanField(default=False)
    responsable_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='customers_as_responsable')  # noqa
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.username


class TripCustomer(models.Model):
    customer_id = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True, default=None)  # noqa
    trip_id = models.ForeignKey(
        Trip, on_delete=models.SET_NULL, null=True, blank=True, default=None)  # noqa
    registred_at = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)
    canceled_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.trip_id.title} - {self.customer_id.user_id.username}"
