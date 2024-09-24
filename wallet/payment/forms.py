# forms.py
from django import forms
from .models import TransactionType, PaymentAccount, Transaction

class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = ['name', 'description']


class PaymentAccountForm(forms.ModelForm):
    class Meta:
        model = PaymentAccount
        fields = ['customer', 'account_no', 'balance', 'status']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender_account', 'destination_account', 'amount', 'description', 'transaction_type', 'reference']
