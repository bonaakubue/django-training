from django.urls import path
from .views import TransactionTypeListView, TransactionTypeCreateView, TransactionTypeDetailView, TransactionTypeUpdateView, TransactionTypeDeleteView

urlpatterns = [
    path('transaction_type', TransactionTypeListView.as_view(), name='transaction_type_list'),
    path('transaction_type/create/', TransactionTypeCreateView.as_view(), name='transaction_type_create'),
    path('transaction_type/<int:pk>/', TransactionTypeDetailView.as_view(), name='transaction_type_detail'),
    path('transactiontype/<int:pk>/update/', TransactionTypeUpdateView.as_view(), name='transaction_type_update'),
    path('transactiontype/<int:pk>/delete/', TransactionTypeDeleteView.as_view(), name='transaction_type_delete')
]
