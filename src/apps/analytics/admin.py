from django.contrib import admin
from .models import ContentScore

# Register your models here.
@admin.register(ContentScore)
class ContentScoreAdmin(admin.ModelAdmin):
    list_display = ['content', 'engagement_score', 'quality_score', 'updated_at']