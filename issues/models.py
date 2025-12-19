from django.db import models
from django.contrib.auth.models import User


class Issues(models.Model):
    SEVERITY_CHOICES = [
        ('CRITICAL', 'critical'),
        ('HIGH','high'),
        ('MEDIUM','medium'),
        ('LOW','low'),
    ]

    STATUS_CHOICES = [
        ('OPEN','open'),
        ('IN_PROGRESS','in_progress'),
        ('FIXED','fixed'),
        ('VERIFIED','verified'),
        ('CLOSED','closed'),
    ]
  
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices= SEVERITY_CHOICES)
    status = models.CharField(max_length=15, choices = STATUS_CHOICES,default='OPEN')

    created_by = models.ForeignKey(User, on_delete = models.CASCADE,related_name='created_issues')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title