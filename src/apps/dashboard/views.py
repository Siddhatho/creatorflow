from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.workflow.models import Content, Campaign

# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    contents = Content.objects.filter(creator=user).order_by('-created_at')

    status_counts = {
        'draft': contents.filter(status='draft').count(),
        'review': contents.filter(status='review').count(),
        'approved': contents.filter(status='approved').count(),
        'scheduled': contents.filter(status='scheduled').count(),
        'published': contents.filter(status='published').count(),
    }

    recent_contents = contents[:5]
    campaigns = Campaign.objects.filter(owner=user).order_by('-created_at')[:5]

    return render(request, 'dashboard/dashboard.html', {
        'status_counts': status_counts,
        'recent_contents': recent_contents,
        'campaigns': campaigns,
        'total': contents.count(),
    })