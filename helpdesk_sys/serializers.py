from rest_framework import serializers
from .models import Issue, IssueResponse

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['user'] 


class IssueResponseSerializer(serializers.ModelSerializer):
    issue = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all())

    class Meta:
        model = IssueResponse
        fields = '__all__'