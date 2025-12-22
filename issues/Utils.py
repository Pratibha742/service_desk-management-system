# helper function
def get_user_role(user):
    if user.is_superuser:
        return "Admin"
    
    if user.groups.filter(name="Admin").exists():
        return "Admin"
    
    if user.groups.filter(name="Support").exists():
        return "Support"
    
    if user.groups.filter(name="Developer").exists():
        return "Developer"
    
    if user.groups.filter(name="Client").exists():
        return "Client"
    
    return None