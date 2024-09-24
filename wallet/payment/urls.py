from django.urls import path
from .views import TransactionTypeListView, TransactionTypeCreateView, TransactionTypeDetailView, TransactionTypeUpdateView, TransactionTypeDeleteView

urlpatterns = [
    path('transaction_type', TransactionTypeListView.as_view(), name='transaction_type_list'),
    path('transaction_type/create/', TransactionTypeCreateView.as_view(), name='transaction_type_create'),
    path('transaction_type/<int:pk>/', TransactionTypeDetailView.as_view(), name='transaction_type_detail'),
    path('transactiontype/<int:pk>/update/', TransactionTypeUpdateView.as_view(), name='transaction_type_update'),
    path('transactiontype/<int:pk>/delete/', TransactionTypeDeleteView.as_view(), name='transaction_type_delete')
]
from django.urls import path
from .views import (
    TransactionTypeListView, TransactionTypeCreateView, TransactionTypeDetailView, 
    TransactionTypeUpdateView, TransactionTypeDeleteView,
    PaymentAccountListView, PaymentAccountCreateView, PaymentAccountUpdateView, 
    PaymentAccountDeleteView, TransactionListView, TransactionCreateView, 
    TransactionUpdateView, TransactionDeleteView
)

urlpatterns = [
    # URLs for TransactionType
    path('transaction_type/', TransactionTypeListView.as_view(), name='transaction_type_list'),
    path('transaction_type/create/', TransactionTypeCreateView.as_view(), name='transaction_type_create'),
    path('transaction_type/<int:pk>/', TransactionTypeDetailView.as_view(), name='transaction_type_detail'),
    path('transaction_type/<int:pk>/update/', TransactionTypeUpdateView.as_view(), name='transaction_type_update'),
    path('transaction_type/<int:pk>/delete/', TransactionTypeDeleteView.as_view(), name='transaction_type_delete'),

    # URLs for PaymentAccount
    path('payment_account/', PaymentAccountListView.as_view(), name='payment_account_list'),
    path('payment_account/create/', PaymentAccountCreateView.as_view(), name='payment_account_create'),
    path('payment_account/<int:pk>/update/', PaymentAccountUpdateView.as_view(), name='payment_account_update'),
    path('payment_account/<int:pk>/delete/', PaymentAccountDeleteView.as_view(), name='payment_account_delete'),

    # URLs for Transaction
    path('transaction/', TransactionListView.as_view(), name='transaction_list'),
    path('transaction/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
]
