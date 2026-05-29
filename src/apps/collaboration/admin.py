from django.contrib import admin
from .models import Comment
from .models import ApprovalRequest

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'parent', 'created_at']
    list_filter = ['created_at']

@admin.register(ApprovalRequest)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ['reviewer', 'content', 'status', 'reviewed_at']
    list_filter = ['status']