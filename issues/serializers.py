from rest_framework import serializers
from .models import Issues

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Issues
        fields = '__all__'