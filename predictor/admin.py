from django.contrib import admin
from .models import HeartData,DoctorHospital,ContactModel
# Register your models here.
admin.site.register(HeartData)
admin.site.register(DoctorHospital)
admin.site.register(ContactModel)