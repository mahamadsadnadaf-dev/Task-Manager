from rest_framework import serializers
from tasks.models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'owner', 'title', 'description', 'status', 'timestamp']
        read_only_fields = ['owner']