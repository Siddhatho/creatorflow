from django.db import models
from apps.workflow.models import Content

# Create your models here.
class ContentScore(models.Model):
    content = models.OneToOneField(Content, on_delete=models.CASCADE, related_name='score')
    engagement_score = models.FloatField(default=0.0)
    quality_score = models.FloatField(default=0.0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Scores for {self.content}"