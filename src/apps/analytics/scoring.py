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

def predict_virality(content):
    """Rule-based virality prediction"""
    score = 0

    # engagement signals
    comment_count = content.comments.count()
    if comment_count >= 5: score += 30
    elif comment_count >= 2: score += 15

    # quality signals
    if content.hashtags: score += 15
    if content.seo_tags: score += 10

    # approval signal
    if content.approvals.filter(status='approved').exists(): score += 20

    # body length signal
    if content.body and len(content.body) > 200: score += 15
    elif content.body and len(content.body) > 100: score += 8

    # AI was used
    if content.activities.filter(event_type='ai_generation').exists(): score += 10

    score = min(score, 100)

    if score >= 70:
        label = 'High'
        color = 'green'
    elif score >= 40:
        label = 'Medium'
        color = 'yellow'
    else:
        label = 'Low'
        color = 'red'

    return {'score': score, 'label': label, 'color': color}

def recommend_posting_time(content):
    """Rule-based best posting time by platform"""
    platform = content.platform.name.lower() if content.platform else 'general'

    schedule = {
        'instagram': {'day': 'Wednesday', 'time': '11:00 AM', 'reason': 'Peak engagement mid-week'},
        'youtube':   {'day': 'Friday',    'time': '03:00 PM', 'reason': 'Weekend prep viewership spike'},
        'linkedin':  {'day': 'Tuesday',   'time': '09:00 AM', 'reason': 'Professional hours, early week'},
        'x':         {'day': 'Wednesday', 'time': '09:00 AM', 'reason': 'Morning trending window'},
        'twitter':   {'day': 'Wednesday', 'time': '09:00 AM', 'reason': 'Morning trending window'},
        'general':   {'day': 'Wednesday', 'time': '10:00 AM', 'reason': 'General peak engagement window'},
    }

    result = schedule.get(platform, schedule['general'])
    result['platform'] = platform.capitalize()
    return result