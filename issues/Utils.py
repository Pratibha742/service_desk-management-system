from django.utils import timezone
from .constants import SLA_RULES

def calculate_due_date(priority):
    now = timezone.now()
    sla_duration = SLA_RULES.get(priority)
    if not sla_duration:
        return None
    return now + sla_duration

def check_sla_breach(issue):
    if issue.due_at and timezone.now() > issue.due_at:
        return True
    return False

# helper function
def get_user_role(user):
    if  not user or not user.is_authenticated:
        return None
    
    if user.is_superuser or user.groups.filter(name="Admin").exists():
        return "Admin"
    
    if user.groups.filter(name="Support").exists():
        return "Support"
    
    if user.groups.filter(name="Developer").exists():
        return "Developer"
    
    if user.groups.filter(name="Client").exists():
        return "Client"
    
    return None