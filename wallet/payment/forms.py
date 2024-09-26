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
    sender_account_no = forms.CharField(
        label="Sender Account Number",
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    destination_account_no = forms.CharField(
        label="Receiver Account Number",
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Transaction
        fields = ['amount', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }