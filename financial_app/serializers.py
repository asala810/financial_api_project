from rest_framework import serializers
from .models import Transaction
from django.contrib.auth.models import User

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_date', 'description', 'amount', 'user_id'] # "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] #معلومات عن اليوزر 