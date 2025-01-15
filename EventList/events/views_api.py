from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .serializers import CustomUserSerializer, EventSerializer, EventUpdateSerializer
from .models import Event, CustomUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnlyCust
from rest_framework.response import Response
from rest_framework.views import APIView


class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication, )

    def list(self, request):
        try:
            queryset = Event.objects.all()
            serializer = EventSerializer(queryset, many=True)
        except Event.DoesNotExist:
            return Response({'error': 'Ошибка', 'result': None})
        else:
            return Response({'error': None, 'result': serializer.data})


class EventRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = (IsOwnerOrReadOnlyCust,)


class AddUserToEvent(generics.RetrieveUpdateAPIView):
    queryset = Event
    serializer_class = EventUpdateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.participants.add(request.user)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class RemoveUserFromEvent(generics.RetrieveUpdateAPIView):
    queryset = Event
    serializer_class = EventUpdateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.participants.remove(request.user)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
