from rest_framework import serializers
from .models import Issue
from user_management.serializers import UserSerializer
from user_management.models import User

class IssueSerializer(serializers.ModelSerializer):
    user = serializers.UUIDField()

    class Meta:
        model = Issue
        fields = ['id', 'issue_description', 'category', 'urgency_level', 'submitted_on', 'user', 'status']