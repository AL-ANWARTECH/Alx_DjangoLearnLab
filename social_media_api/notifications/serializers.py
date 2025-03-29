from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id', 'actor', 'verb', 'target', 
            'read', 'timestamp'
        ]

    def get_target(self, obj):
        if obj.target:
            return str(obj.target)
        return None