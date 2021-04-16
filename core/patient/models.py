from django.db import models
from django.urls import reverse

class Patient(models.Model):
    hospital_number = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)
    postcode = models.CharField(max_length=10)
    locality = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('patient:single', args=[self.id])

class D2A(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    completion_date = models.CharField(max_length=200)
    extra_info = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('patient:d2a', args=[self.id])