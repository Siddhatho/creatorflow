from .models import ActivityLog

def log_activity(content, user, event_type, detail=''):
    ActivityLog.objects.create(
        content=content,
        user=user,
        event_type=event_type,
        detail=detail
    )