from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'email', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
