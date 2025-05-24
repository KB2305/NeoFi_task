from rest_framework import serializers
from .models import Event, EventPermission, EventVersion, User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at')

class EventPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPermission
        fields = '__all__'

class EventVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVersion
        fields = '__all__'