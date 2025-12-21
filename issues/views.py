# from django import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Issues
from .serializers import IssueSerializer
from .permissions import IsClient, IsDeveloper, IsSupportOrAdmin


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
         # Base queryset (replacement for queryset = Issue.objects.filter(...))
        queryset = Issues.objects.filter(is_deleted = False)

        # Admin & Support → all issues
        if user.groups.filter(name__in = ["Support", "Admin"]).exists():
            return queryset
        # Developer → only assigned issues
        if user.groups.filter(name= "Developer").exists():
            return queryset.filter(assigned_to=user)
         # Client → only own issues
        return queryset.filter(created_by=user)
    
    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user)
    
