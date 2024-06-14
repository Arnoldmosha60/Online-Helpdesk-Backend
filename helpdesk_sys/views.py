from django.shortcuts import render
from .serializers import IssueSerializer
from .models import Issue
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user_management.models import User

# Create your views here.
class IssueListCreateView(APIView):
    def get(self, request):
        issue = Issue.objects.all()
        serializer = IssueSerializer(issue, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data

        # Extract user details
        user_id = data.get('user')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create or update the issue
        serializer = IssueSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)  # Assign the User instance to the 'user' field
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssueDetailView(APIView):
    def get_object(self, pk):
        try:
            return Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        issue = self.get_object(pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)
    
    def put(self, request, pk):
        issue = self.get_object(pk)
        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        issue = self.get_object(pk)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
