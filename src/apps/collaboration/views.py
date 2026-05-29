from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.users.decorators import reviewer_required
from .models import ApprovalRequest
from django.views.decorators.http import require_POST
from apps.workflow.models import Content
from .models import Comment

# Create your views here.
@login_required
@require_POST
def add_comment(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    body = request.POST.get('body', '').strip()
    parent_id = request.POST.get('parent_id')
    if body:
        parent = Comment.objects.get(pk=parent_id) if parent_id else None
        Comment.objects.create(content=content, author=request.user, body=body, parent=parent)
    return redirect('workflow:content_detail', pk=content_id)


@login_required
@reviewer_required
@require_POST
def review_content(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    action = request.POST.get('action')  # 'approved' or 'rejected'
    feedback = request.POST.get('feedback', '').strip()

    if action in ['approved', 'rejected']:
        ApprovalRequest.objects.update_or_create(
            content=content,
            reviewer=request.user,
            defaults={'status': action, 'feedback': feedback}
        )
        # Advance content status if approved
        if action == 'approved':
            content.status = 'approved'
            content.save()

    return redirect('workflow:content_detail', pk=content_id)