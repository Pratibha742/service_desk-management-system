from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Issues
from .serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
    queryset = Issues.objects.filter(is_deleted = False)
    serializer_class = IssueSerializer
    
