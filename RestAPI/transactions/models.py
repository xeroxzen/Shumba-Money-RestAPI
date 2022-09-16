from django.db import models
import uuid

# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey("users.Customer", on_delete=models.CASCADE, related_name="sender")
    recipient = models.ForeignKey("recipients.Recipient", on_delete=models.CASCADE, related_name="recipient")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")
    transaction_type = models.CharField(max_length=20, default="transfer")
    reference = models.CharField(max_length=20, default="")

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