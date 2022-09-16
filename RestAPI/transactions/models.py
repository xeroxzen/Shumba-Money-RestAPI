from django.db import models
import uuid

TRANSACTION_STATUSES = (
    ("pending", "Pending"),
    ("success", "Success"),
    ("failed", "Failed"),
    ("cancelled", "Cancelled"),
    ('refunded', 'Refunded'),
    ('reversed', 'Reversed'),
    ('chargeback', 'Chargeback'),
    ('disputed', 'Disputed'),
    ('expired', 'Expired'),
    ('declined', 'Declined'),
    ('authorized', 'Authorized'),
    ('captured', 'Captured'),
    ('voided', 'Voided'),
    ('settled', 'Settled'),
)

TRANSACTION_TYPES = (
    ("credit", "Credit"),
    ("debit", "Debit"),
    ("transfer", "Transfer"),
)

# function to generate a unique reference number
def generate_reference():
    return uuid.uuid4().hex[:6].upper()


# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey("users.Customer", on_delete=models.CASCADE, related_name="customer")
    recipient = models.ForeignKey("recipients.Recipient", on_delete=models.CASCADE, related_name="recipient")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending", choices=TRANSACTION_STATUSES)
    transaction_type = models.CharField(max_length=20, default="transfer", choices=TRANSACTION_TYPES)
    reference = models.CharField(max_length=20, default=generate_reference, unique=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender} sent {self.amount} to {self.recipient}"

    def save(self, *args, **kwargs):
        if self.transaction_type == "transfer":
            self.sender.balance -= self.amount
            self.recipient.balance += self.amount
            self.sender.save()
            self.recipient.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.transaction_type == "transfer":
            self.sender.balance += self.amount
            self.recipient.balance -= self.amount
            self.sender.save()
            self.recipient.save()
        super().delete(*args, **kwargs)