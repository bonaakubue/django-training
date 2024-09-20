from django.db import models
from django.contrib.auth.models import User

class TransactionType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class PaymentAccount(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('dormant', 'Dormant'),
        ('suspended', 'Suspended')
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class Transaction(models.Model):
    sender_account = models.ForeignKey(PaymentAccount, on_delete=models.CASCADE, related_name='sent_transactions')
    destination_account = models.ForeignKey(PaymentAccount, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    description = models.TextField()
    transaction_date = models.DateTimeField(auto_now=True)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    reference = models.CharField(max_length=20, unique=True)
