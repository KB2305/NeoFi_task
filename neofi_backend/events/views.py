from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event, EventPermission, EventVersion
from .serializers import RegisterSerializer, EventSerializer, EventPermissionSerializer, EventVersionSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrEditor

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(permissions__user=self.request.user)

    def perform_create(self, serializer):
        event = serializer.save(created_by=self.request.user)
        EventPermission.objects.create(event=event, user=self.request.user, role='owner')

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEditor]

    def perform_update(self, serializer):
        instance = serializer.save()
        EventVersion.objects.create(event=instance, data=EventSerializer(instance).data, created_by=self.request.user)

class ShareEventView(APIView):
    permission_classes = [IsOwnerOrEditor]

    def post(self, request, id):
        event = get_object_or_404(Event, id=id)
        if not EventPermission.objects.filter(event=event, user=request.user, role='owner').exists():
            return Response({'detail': 'Only owners can share events.'}, status=403)

        for user_data in request.data.get('users', []):
            user = get_object_or_404(User, id=user_data['user_id'])
            EventPermission.objects.update_or_create(event=event, user=user, defaults={'role': user_data['role']})
        return Response({'detail': 'Permissions updated.'})

class EventHistoryView(generics.ListAPIView):
    serializer_class = EventVersionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EventVersion.objects.filter(event__id=self.kwargs['id'])

class EventRollbackView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id, versionId):
        version = get_object_or_404(EventVersion, version_id=versionId, event__id=id)
        event = version.event
        serializer = EventSerializer(event, data=version.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Rolled back to previous version.'})