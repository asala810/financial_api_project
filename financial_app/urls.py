from django.urls import path
from .views import (
    TransactionListCreate ,
    TransactionDetail,
    UserListView ,
    UserTransactionsView,
    ReportView,
)

urlpatterns = [
    path('transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:user_id>/transactions/', UserTransactionsView.as_view(), name='user-transactions'),
    path('reports/', ReportView.as_view(), name='reports'),
 # بربطها ب financial_api.urls .. دي الحاجات اللي هنعمل بيها test
]