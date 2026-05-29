from django.contrib import admin
from .models import Comment
from .models import ApprovalRequest
from .models import ActivityLog

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'parent', 'created_at']
    list_filter = ['created_at']

@admin.register(ApprovalRequest)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ['reviewer', 'content', 'status', 'reviewed_at']
    list_filter = ['status']


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ['event_type', 'user', 'content', 'created_at']
    list_filter = ['event_type']