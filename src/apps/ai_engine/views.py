from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .services import AIService
from .prompts import PromptManager
from .parsers import ResponseParser
from django.views.decorators.http import require_POST
from apps.workflow.models import Content
from apps.collaboration.utils import log_activity

# Create your views here.
@login_required
def ai_test(request):
    service = AIService()
    prompt = PromptManager.content_summarize("CreatorFlow OS is an AI-powered creator workflow platform built with Django.")
    raw = service.generate(prompt)
    result = ResponseParser.parse_summary(raw)
    return JsonResponse({'summary': result})

@login_required
def ai_models(request):
    import google.generativeai as genai
    from django.conf import settings
    genai.configure(api_key=settings.GEMINI_API_KEY)
    models = [m.name for m in genai.list_models()]
    return JsonResponse({'models': models})

@login_required
@require_POST
def generate_caption(request, content_id):
    content = get_object_or_404(Content, pk=content_id, creator=request.user)
    platform = content.platform.name if content.platform else "General"
    service = AIService()
    prompt = PromptManager.generate_caption(content.body, platform)
    raw = service.generate(prompt)
    caption = ResponseParser.parse_caption(raw)
    log_activity(content, request.user, 'ai_generation', 'Caption generated')
    return JsonResponse({'caption': caption})

@login_required
@require_POST
def adapt_content(request, content_id):
    content = get_object_or_404(Content, pk=content_id, creator=request.user)
    target_platform = request.POST.get('platform', 'instagram')
    service = AIService()
    prompt = PromptManager.adapt_for_platform(content.body, target_platform)
    raw = service.generate(prompt)
    adapted = ResponseParser.parse_adapted_content(raw)
    log_activity(content, request.user, 'ai_generation', f'Adapted for {target_platform}')
    return JsonResponse({'adapted': adapted, 'platform': target_platform})

@login_required
@require_POST
def generate_hashtags(request, content_id):
    content = get_object_or_404(Content, pk=content_id, creator=request.user)
    platform = content.platform.name if content.platform else "General"
    service = AIService()
    prompt = PromptManager.generate_hashtags(content.title, content.body, platform)
    raw = service.generate(prompt)
    result = ResponseParser.parse_hashtags(raw)
    # save to content
    content.hashtags = result['hashtags']
    content.seo_tags = result['seo_tags']
    content.save()
    log_activity(content, request.user, 'ai_generation', 'Hashtags & SEO tags generated')
    return JsonResponse(result)