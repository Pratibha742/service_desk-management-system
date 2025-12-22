from rest_framework import serializers
from .models import Issues
from .constants import ROLE_STATUS_TRANSITIONS
from .Utils import get_user_role

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Issues
        fields = '__all__'
        read_only_fields = ["id"]

    def validate_status(self, new_status):
        request = self.context.get("request")
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

        if role not in allowed_next:
            raise serializers.ValidationError(
                f"{role} cannot cha ge status from "
                f"{current_status} to {new_status}"
            )
        return new_status