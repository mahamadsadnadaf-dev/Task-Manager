from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Tasks
from django.shortcuts import render

class IsOwnerOrForbidden(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    
class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrForbidden]

    def get_queryset(self):
        return Tasks.objects.filter(owner=self.request.user).order_by('-timestamp')
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    
    @action(detail=True, methods=['post'])
    def toggle(self,request,pk=None):
        task = self.get_object()
        task.status = not task.status
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def dashboard_view(request):
        return render(request, 'index.html')
