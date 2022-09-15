import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, editable=True, blank=False)
    middle_name = models.CharField(max_length=100, editable=True, blank=True)
    last_name = models.CharField(max_length=100, editable=True, blank=False)
    email = models.EmailField(max_length=100, editable=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=False, editable=True)
    country_of_residence = models.CharField(max_length=100, editable=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # recipients = models.ManyToManyField(Recipients, blank=True)


    class Meta:
        ordering = ["-created_at"]

    # Use fstrings
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    @classmethod
    def get_full_name(cls):
        return f"{cls.first_name} {cls.middle_name} {cls.last_name}"

    @classmethod
    def get_user_by_email(cls):
        return cls.objects.get(email=cls.email)
    
    @classmethod
    def get_total_users(cls):
        return cls.objects.all().count()
    
