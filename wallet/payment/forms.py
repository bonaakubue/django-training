from django.forms import ModelForm
from .models import PaymentAccount, TransactionType, Transaction

class TransactionTypeForm(ModelForm):
    class Meta:
        model = TransactionType
        fields = ['name', 'description']