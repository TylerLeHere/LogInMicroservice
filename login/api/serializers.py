from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phn', 'name', 'password']
        extra_kwargs = {
            'password' : {'write_only' : True} # dont show password when returning user
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # validated data without password
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('__all__')

# class HistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HealthHistory
#         fields = ('__all__')