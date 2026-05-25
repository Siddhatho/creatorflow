from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .services import AIService
from .prompts import PromptManager
from .parsers import ResponseParser

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