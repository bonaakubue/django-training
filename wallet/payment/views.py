from django.shortcuts import render
from .models import TransactionType, Transaction, PaymentAccount
from .forms import TransactionTypeForm, PaymentAccountForm, TransactionForm
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView
)
from django.urls import reverse_lazy

# TransactionType Views
class TransactionTypeListView(ListView):
    model = TransactionType
    template_name = 'payment/transaction_type_list.html'
    context_object_name = 'transactiontypes'

class TransactionTypeCreateView(CreateView):
    model = TransactionType
    template_name = 'payment/transaction_type_create.html'
    form_class = TransactionTypeForm
    success_url = reverse_lazy('transaction_type_list')

class TransactionTypeDetailView(DetailView):
    model = TransactionType
    template_name = 'payment/transaction_type_detail.html'
    context_object_name = 'transactiontype'

class TransactionTypeUpdateView(UpdateView):
    model = TransactionType
    form_class = TransactionTypeForm
    template_name = 'payment/transaction_type_update.html'
    success_url = reverse_lazy('transaction_type_list')

class TransactionTypeDeleteView(DeleteView):
    model = TransactionType
    template_name = 'payment/transaction_type_delete.html'
    success_url = reverse_lazy('transaction_type_list') 

# PaymentAccount Views
class PaymentAccountListView(ListView):
    model = PaymentAccount
    template_name = 'payment/payment_account_list.html'
    context_object_name = 'payment_accounts'

class PaymentAccountCreateView(CreateView):
    model = PaymentAccount
    form_class = PaymentAccountForm  # Use the PaymentAccountForm instead of fields
    template_name = 'payment/payment_account_create.html'
    success_url = reverse_lazy('payment_account_list')

class PaymentAccountUpdateView(UpdateView):
    model = PaymentAccount
    form_class = PaymentAccountForm  # Use the PaymentAccountForm instead of fields
    template_name = 'payment/payment_account_update.html'
    success_url = reverse_lazy('payment_account_list')

class PaymentAccountDeleteView(DeleteView):
    model = PaymentAccount
    template_name = 'payment/payment_account_delete.html'
    success_url = reverse_lazy('payment_account_list')

# Transaction Views
class TransactionListView(ListView):
    model = Transaction
    template_name = 'payment/transaction_list.html'
    context_object_name = 'transactions'

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm  # Use the TransactionForm instead of fields
    template_name = 'payment/transaction_create.html'
    success_url = reverse_lazy('transaction_list')

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm  # Use the TransactionForm instead of fields
    template_name = 'payment/transaction_update.html'
    success_url = reverse_lazy('transaction_list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'payment/transaction_delete.html'
    success_url = reverse_lazy('transaction_list')
