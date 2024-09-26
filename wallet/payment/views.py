from django.shortcuts import render, redirect
from .models import TransactionType, Transaction, PaymentAccount
from .forms import TransactionTypeForm, PaymentAccountForm, TransactionForm
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView, 
)
import uuid 
from django.urls import reverse_lazy
from django.contrib import messages

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
    form_class = TransactionForm
    template_name = 'payment/transaction_create.html'
    success_url = reverse_lazy('transaction_list')

    def form_valid(self, form):
        sender_account_no = form.cleaned_data['sender_account_no']
        destination_account_no = form.cleaned_data['destination_account_no']
        amount = form.cleaned_data['amount']

        try:
            sender_account = PaymentAccount.objects.get(account_no=sender_account_no)
            destination_account = PaymentAccount.objects.get(account_no=destination_account_no)
        except PaymentAccount.DoesNotExist:
            form.add_error(None, "Invalid sender or receiver account number.")
            return self.form_invalid(form)

        # Check if the sender has enough balance
        if sender_account.balance < amount:
            form.add_error('amount', "Insufficient funds in the sender's account.")
            return self.form_invalid(form)

        # Perform the debit and credit transactions
        sender_account.balance -= amount
        destination_account.balance += amount

        # Save the updated balances
        sender_account.save()
        destination_account.save()

        # Set the transaction type to "debit"
        try:
            transaction_type_debit = TransactionType.objects.get(name="debit")
        except TransactionType.DoesNotExist:
            messages.error(self.request, "Transaction type 'debit' is missing. Please add it to the system.")
            return self.form_invalid(form)

        # Generate a unique reference using uuid
        reference = str(uuid.uuid4())[:12]  # Create a 12-character unique reference

        # Save the transaction
        transaction = form.save(commit=False)
        transaction.sender_account = sender_account
        transaction.destination_account = destination_account
        transaction.transaction_type = transaction_type_debit
        transaction.reference = reference  # Assign the generated reference
        transaction.save()

        messages.success(self.request, "Transaction completed successfully.")
        return redirect(self.success_url)
class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm  # Use the TransactionForm instead of fields
    template_name = 'payment/transaction_update.html'
    success_url = reverse_lazy('transaction_list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'payment/transaction_delete.html'
    success_url = reverse_lazy('transaction_list')
