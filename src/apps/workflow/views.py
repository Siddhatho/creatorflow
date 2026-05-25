from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Content, ContentStatus
from .forms import ContentForm

# Create your views here.
ALLOWED_TRANSITIONS = {
    'draft': 'review',
    'review': 'approved',
    'approved': 'scheduled',
    'scheduled': 'published',
}

@login_required
def content_list(request):
    contents = Content.objects.filter(creator=request.user).order_by('-created_at')
    return render(request, 'workflow/content_list.html', {'contents': contents})

@login_required
def content_create(request):
    form = ContentForm(request.POST or None)
    if form.is_valid():
        content = form.save(commit=False)
        content.creator = request.user
        content.status = 'draft'
        content.save()
        ContentStatus.objects.create(
            content=content, changed_by=request.user,
            from_status='', to_status='draft'
        )
        messages.success(request, 'Content created as Draft.')
        return redirect('workflow:content_list')
    return render(request, 'workflow/content_form.html', {'form': form, 'action': 'Create'})

@login_required
def content_edit(request, pk):
    content = get_object_or_404(Content, pk=pk, creator=request.user)
    form = ContentForm(request.POST or None, instance=content)
    if form.is_valid():
        form.save()
        messages.success(request, 'Content updated.')
        return redirect('workflow:content_list')
    return render(request, 'workflow/content_form.html', {'form': form, 'action': 'Edit'})

@login_required
def content_advance(request, pk):
    content = get_object_or_404(Content, pk=pk)
    next_status = ALLOWED_TRANSITIONS.get(content.status)
    if not next_status:
        messages.error(request, 'No further transitions available.')
        return redirect('workflow:content_list')
    prev = content.status
    content.status = next_status
    content.save()
    ContentStatus.objects.create(
        content=content, changed_by=request.user,
        from_status=prev, to_status=next_status
    )
    messages.success(request, f'Status moved to {next_status}.')
    return redirect('workflow:content_list')

@login_required
def content_detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    history = content.status_history.order_by('changed_at')
    return render(request, 'workflow/content_detail.html', {'content': content, 'history': history})

@login_required
def campaign_list(request):
    campaigns = Campaign.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'workflow/campaign_list.html', {'campaigns': campaigns})

@login_required
def campaign_create(request):
    form = CampaignForm(request.POST or None)
    if form.is_valid():
        campaign = form.save(commit=False)
        campaign.owner = request.user
        campaign.save()
        form.save_m2m()
        messages.success(request, 'Campaign created.')
        return redirect('workflow:campaign_list')
    return render(request, 'workflow/campaign_form.html', {'form': form, 'action': 'Create'})

@login_required
def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk, owner=request.user)
    contents = campaign.contents.all()
    # filtering by platform
    platform_id = request.GET.get('platform')
    if platform_id:
        contents = contents.filter(platform_id=platform_id)
    platforms = campaign.platforms.all()
    return render(request, 'workflow/campaign_detail.html', {
        'campaign': campaign,
        'contents': contents,
        'platforms': platforms,
        'selected_platform': platform_id,
    })

@login_required
def campaign_edit(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk, owner=request.user)
    form = CampaignForm(request.POST or None, instance=campaign)
    if form.is_valid():
        form.save()
        messages.success(request, 'Campaign updated.')
        return redirect('workflow:campaign_list')
    return render(request, 'workflow/campaign_form.html', {'form': form, 'action': 'Edit'})