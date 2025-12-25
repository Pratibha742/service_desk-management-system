from rest_framework import serializers
from .models import Issues
from .models import ChangeRequest
from .constants import ROLE_STATUS_TRANSITIONS
from .Utils import get_user_role, calculate_due_date


class IssueSerializer(serializers.ModelSerializer):
    change_requests = serializers.SerializerMethodField(read_only= True)
    class Meta:
        model  = Issues
        fields = "__all__"
        read_only_fields = ["id","due_at","sla_breached"]

    def get_change_requests(self, obj):
        return ChangeRequestSerializer(
            obj.change_requests.all(),
            many= True
        ).data
        

    def validate_status(self, new_status):
        request = self.context.get("request")
        if not request:
            return new_status
        user = request.user
        

        issue = self.instance  #existing issue
        if not issue:
            return new_status  #creation k time open allowed
        
        current_status = issue.status
        role = get_user_role(user)

        if role == "Admin":
            return new_status

        if role not in ROLE_STATUS_TRANSITIONS:
            raise serializers.ValidationError("Role not allowed")
        
        allowed_next = ROLE_STATUS_TRANSITIONS[role].get(
            current_status, []
        )

        if new_status not in allowed_next:
            raise serializers.ValidationError(
                f"{role} cannot change status from "
                f"{current_status} to {new_status}"
            )
        return new_status
    
    def create(self, validated_data):
        priority = validated_data.get("priority",Issues.PRIORITY_MEDIUM)

        validated_data["due_at"] = calculate_due_date(priority)
        validated_data["sla_breached"] = False

        return super().create(validated_data)  
    
     
class ChangeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeRequest
        fields = [
            "id",
            "issue",
            "field_name",
            "old_value",
            "new_value",
            "status",
            "reason",
            "created_at",
            "requested_by",
            "approved_by",
        ]
        read_only_fields = [
            "status",
            "requested_by",
            "approved_by",
            "old_value",
        ]

    def create(self, validated_data):
        request = self.context["request"]
        issue = validated_data["issue"]
        field = validated_data["field_name"]

        validated_data["requested_by"] = request.user
        validated_data["old_value"] = getattr(issue,field)

        return super().create(validated_data)
