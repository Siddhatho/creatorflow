from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .services import AIService
from .prompts import PromptManager
from .parsers import ResponseParser
from django.views.decorators.http import require_POST
from apps.workflow.models import Content

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
    return JsonResponse({'caption': caption})