from django.db import models
import uuid

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, editable=False, blank=False)
    middle_name = models.CharField(max_length=100, editable=False, blank=True)
    last_name = models.CharField(max_length=100, editable=False, blank=False)
    email = models.EmailField(max_length=100, editable=False, blank=True)
    phone_number = models.CharField(max_length=13, editable=False, blank=False)
    country_of_residence = models.CharField(max_length=100, editable=False, blank=False)
    password = models.CharField(max_length=40, editable=False, blank=False)
    # recipients = models.ManyToManyField(Recipients, blank=True)


    # Use fstrings
    class Meta:
        ordering = ["-first_name"]

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
