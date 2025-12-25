from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


class Issues(models.Model):
    STATUS_OPEN = "OPEN"
    STATUS_IN_PROGRESS = "IN_PROGRESS"
    STATUS_RESOLVED = "RESOLVED"
    STATUS_CLOSED = "CLOSED"

    PRIORITY_HIGH = "HIGH"
    PRIORITY_MEDIUM = "MEDIUM"
    PRIORITY_LOW = "LOW" 
 
    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, "High"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_LOW, "Low")
    ]
    SEVERITY_CHOICES = [
        ('CRITICAL', 'Critical'),
        ('HIGH','High'),
        ('MEDIUM','Medium'),
        ('LOW','Low'),
    ]

    STATUS_CHOICES = [
        (STATUS_OPEN,'Open'),
        (STATUS_IN_PROGRESS,'In_Progress'),
        (STATUS_RESOLVED,'Resolved'),
        (STATUS_CLOSED,'Closed'),
    ]
  
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices= SEVERITY_CHOICES)
    status = models.CharField(max_length=15, choices = STATUS_CHOICES, default=STATUS_OPEN)

    priority =models.CharField(max_length=10, choices= PRIORITY_CHOICES, default=PRIORITY_MEDIUM)
    due_at = models.DateTimeField(null=True, blank=True)
    sla_breached = models.BooleanField(default=False)

    created_by = models.ForeignKey(User, on_delete = models.CASCADE,related_name='created_issues')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
# new model for change request
class ChangeRequest(models.Model):
    FIELD_STATUS = "status"
    FIELD_SEVERITY = "severity"
    FIELD_ASSIGNEE = "assignee"

    FIELD_CHOICES = [
        (FIELD_STATUS, "Status"),
        (FIELD_SEVERITY,"Severity"),
        (FIELD_ASSIGNEE,"Assignee"),
    ]

    STATUS_PENDING = "PENDING"
    STATUS_APPROVED = "APPROVED"
    STATUS_REJECTED = "REJECTED"

    REQUEST_STATUS_CHOICES =[
        (STATUS_PENDING, "Pending"),
        (STATUS_APPROVED,"Approved"),
        (STATUS_REJECTED,"Rejected"),
    ]

    issue= models.ForeignKey(
        Issues,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="change_requests")

    field_name = models.CharField(max_length=20,choices=FIELD_CHOICES)

    old_value = models.CharField(max_length=100)
    new_value = models.CharField(max_length=100)

    requested_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="requested_changes"
    )

    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="approved_changes"
    )

    status = models.CharField(
        max_length=20,
        choices=REQUEST_STATUS_CHOICES,
        default=STATUS_PENDING
    )

    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.field_name} changed Request (Issue ID: ({self.issue.id})"
