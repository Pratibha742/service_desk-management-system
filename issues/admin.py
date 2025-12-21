from django.contrib import admin
from .models import Issues

@admin.register(Issues)
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_by',
        'assigned_to',
        'status',
        'severity',
        'is_deleted',
        'created_at',
    )

    list_filter = ('status','severity','is_deleted')
    search_fields = ('title','description')
    
