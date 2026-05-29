from apps.collaboration.models import Comment, ApprovalRequest, ActivityLog

def calculate_engagement_score(content):
    """Heuristic: based on comments, approvals, AI usage"""
    score = 0
    score += content.comments.count() * 10        # 10 pts per comment
    score += content.comments.filter(parent__isnull=False).count() * 5  # 5 pts per reply
    score += content.approvals.filter(status='approved').count() * 20   # 20 pts per approval
    score += content.activities.filter(event_type='ai_generation').count() * 5  # 5 pts per AI use
    return min(round(score, 2), 100)  # cap at 100

def calculate_quality_score(content):
    """Heuristic: based on content completeness"""
    score = 0
    if content.title and len(content.title) > 5:
        score += 20
    if content.body and len(content.body) > 50:
        score += 20
    if content.hashtags:
        score += 20
    if content.seo_tags:
        score += 20
    if content.platform:
        score += 10
    if content.approvals.filter(status='approved').exists():
        score += 10
    return min(round(score, 2), 100)  # cap at 100

def compute_scores(content):
    from .models import ContentScore
    engagement = calculate_engagement_score(content)
    quality = calculate_quality_score(content)
    ContentScore.objects.update_or_create(
        content=content,
        defaults={'engagement_score': engagement, 'quality_score': quality}
    )
    return engagement, quality