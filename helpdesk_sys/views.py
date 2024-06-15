from django.http import Http404
from django.shortcuts import render
from .serializers import IssueSerializer
from .models import Issue
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from user_management.models import User
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class IssueListCreateView(APIView):
    def get(self, request):
        issues = Issue.objects.select_related('user').all() 
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        user_id = data.get('user')
        
        if not user_id:
            return Response({"detail": "User ID was not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Attach the user's ID
        data['user'] = user.id  

        serializer = IssueSerializer(data=data)
        if serializer.is_valid():
            # Save the issue with the found user
            serializer.save(user=user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssueDetailView(APIView):

    def get_object(self, id):
        try:
            return Issue.objects.get(id=id)
        except Issue.DoesNotExist:
            raise Http404  # Use Http404 instead of returning a Response

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404
        
        # Ensure that the requesting user can only fetch their own issues
        # if request.user.id != user.id:
        #     return Response(status=status.HTTP_403_FORBIDDEN)

        issues = Issue.objects.filter(user=user)
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)
    
    def put(self, request, user_id):
        issue = self.get_object(user_id)
        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        issue = self.get_object(user_id)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
