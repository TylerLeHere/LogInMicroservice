#Take models and has all of the python related code, translate all of these keys into Json
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'username', 'password', 'remember_me', 'votes_to_skip', 'created_at')