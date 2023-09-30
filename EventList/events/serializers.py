from rest_framework import serializers
from .models import CustomUser, Event


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')


class EventSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = '__all__'


class EventUpdateSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['participants']