# from django import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Issues
from .models import ChangeRequest
from .serializers import ChangeRequestSerializer
from .serializers import IssueSerializer
from .permissions import IsClient, IsDeveloper, IsSupportOrAdmin
from .Utils import calculate_due_date


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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
    
class ChangeRequestViewSet(ModelViewSet):
    queryset = ChangeRequest.objects.all()
    serializer_class = ChangeRequestSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="Admin").exists():
            return self.queryset
        return self.queryset.filter(requested_by=user)

    @action(detail=True, methods=["post"])
    def approve(self, request, pk= None):
        change_request = self.get_object()

        if not request.user.groups.filter(name="Admin").exists():
            return Response(
                {"error":"Only Admin can Approve"},
                status=status.HTTP_403_FORBIDDEN
            ) 
        
        issue = change_request.issue
        field = change_request.field_name

        serializer = IssueSerializer(
            issue,
            data = {field: change_request.new_value},
            partial = True,
            context = {"request":request}
            )
        
        serializer.is_valid(raise_exception= True)
        serializer.save()

        if field == "priority":
            issue.due_at = calculate_due_date(change_request.new_value)
            issue.sla_breached = False
            issue.save() 

        change_request.status = ChangeRequest.STATUS_APPROVED
        change_request.approved_by = request.user
        change_request.save()
        
        return Response({"message": "Change Approved"})
    
    @action(detail=True,methods=["post"])
    def reject(self,request,pk=None):
        change_request = self.get_object()

        if not request.user.groups.filter(name="Admin").exists():
            return Response(
                {"error": "Only Admin can Reject"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        change_request.status = ChangeRequest.STATUS_REJECTED
        change_request.approved_by = request.user
        change_request.save()

        return Response({"message": "Change Rejected"})
    


    
