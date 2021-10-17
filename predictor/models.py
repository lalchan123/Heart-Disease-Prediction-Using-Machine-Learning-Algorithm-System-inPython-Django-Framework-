from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

class HeartData(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.FloatField()
    trestbps = models.FloatField()
    chol = models.FloatField()
    fbs = models.FloatField()
    restcg = models.FloatField()
    thalach = models.FloatField()
    exang = models.FloatField()
    oldpeak = models.FloatField()
    slope = models.FloatField()
    ca = models.FloatField()
    thal = models.FloatField()
    owner = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , related_name='owner' , null=True)
    date = models.DateField(auto_now_add=True)
    probability = models.FloatField(null=True)

    def __str__(self):
        return '{} {}'.format(self.owner , self.pk)

class DoctorHospital(models.Model):
    doctor_name = models.CharField(max_length=25)
    hospital_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_no = models.CharField(max_length=25)
    Location = models.CharField(max_length=25)

    def __str__(self):
        return self.doctor_name +" "+ self.hospital_name

    
class ContactModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    title=models.CharField(max_length=250)
    message=models.TextField()

    def __str__(self):
        return self.email