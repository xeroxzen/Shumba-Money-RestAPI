from django.db import models
import uuid

COUNTRIES = (
    ('ZW', 'Zimbabwe'),
    ('KE', 'Kenya'),
)

class Recipient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, blank=False, editable=True)
    middle_name = models.CharField(max_length=50,blank=True,editable=True)
    last_name = models.CharField(max_length=50, blank=False,editable=True)
    email = models.EmailField(max_length=100, blank=True,editable=True)
    phone_number = models.CharField(max_length=50,editable=True)
    country_of_residence = models.CharField(max_length=50, choices=COUNTRIES,editable=True, blank=False)
    city_or_town = models.CharField(max_length=50,editable=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # transactions = models.ManyToManyField(Transaction, blank=True)

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.first_name

    @classmethod
    def get_full_name(cls):
        return f"{cls.first_name} {cls.middle_name} {cls.last_name}"

    @classmethod
    def get_user_by_email(cls):
        return cls.objects.get(email=cls.email)
    
    @classmethod
    def get_total_users(cls):
        return cls.objects.all().count()
    
