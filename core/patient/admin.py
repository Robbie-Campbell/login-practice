from django.contrib import admin
from .models import Patient, D2A

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    def __str__(self):
        return "Patient"

@admin.register(D2A)
class D2AAdmin(admin.ModelAdmin):
    def __str__(self):
        return "Discharge to Assess"

