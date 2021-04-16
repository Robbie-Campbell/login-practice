from django.db import models

class Patient(models.Model):
    hospital_number = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)
    postcode = models.CharField(max_length=10)
    locality = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"