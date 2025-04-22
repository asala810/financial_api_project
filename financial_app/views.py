#from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer ,  UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.db.models import Sum


class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer    

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserTransactionsView(APIView):
    def get(self, request, user_id):
        transactions = Transaction.objects.filter(user_id=user_id)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    
class ReportView(APIView): #التقرير المطلوب مني 
    def get(self, request):
        user_id = request.query_params.get('user_id')  
        year = request.query_params.get('year') #كل سنه 
        month = request.query_params.get('month') #كل شهر 
        
        if not user_id or not year: #لو متحطوش هيطلع ايرور 
            return Response({'error': 'user_id and year are required'}, status=400)

        
        transactions = Transaction.objects.filter(user_id=user_id, transaction_date__year=year)
        
        if month:  
            transactions = transactions.filter(transaction_date__month=month)
        
        total_amount = transactions.aggregate(Sum('amount'))['amount__sum'] or 0  # إجمالي المبلغ

        
        return Response({
            'user_id': user_id,
            'year': year,
            'month': month,
            'total_amount': total_amount,
            'transaction_count': transactions.count()
        })