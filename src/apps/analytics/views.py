from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from apps.workflow.models import Content
from .scoring import compute_scores
from .models import ContentScore

# Create your views here.

@login_required
@require_POST
def refresh_scores(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    engagement, quality = compute_scores(content)
    return JsonResponse({'engagement_score': engagement, 'quality_score': quality})

@login_required
def score_summary(request):
    scores = ContentScore.objects.select_related('content').order_by('-engagement_score')[:10]
    data = [
        {
            'title': s.content.title,
            'engagement': s.engagement_score,
            'quality': s.quality_score,
        }
        for s in scores
    ]
    return JsonResponse({'scores': data})