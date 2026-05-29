from django.contrib import admin
from .models import ContentScore
from .models import ViralityPrediction

# Register your models here.
@admin.register(ContentScore)
class ContentScoreAdmin(admin.ModelAdmin):
    list_display = ['content', 'engagement_score', 'quality_score', 'updated_at']


@admin.register(ViralityPrediction)
class ViralityAdmin(admin.ModelAdmin):
    list_display = ['content', 'label', 'score', 'updated_at']