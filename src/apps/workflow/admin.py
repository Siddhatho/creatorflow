from django.contrib import admin
from .models import Platform, Campaign, Content, ContentStatus

# Register your models here.
admin.site.register(Platform)
admin.site.register(Campaign)
admin.site.register(ContentStatus)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'campaign', 'platform', 'status', 'created_at']
    list_filter = ['status', 'platform', 'campaign']
    search_fields = ['title']
    readonly_fields = ['hashtags', 'seo_tags']