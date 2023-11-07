from rest_framework import serializers
from .models import User, HealthHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthHistory
        fields = ('__all__')