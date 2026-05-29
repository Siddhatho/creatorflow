from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('scores/refresh/<int:content_id>/', views.refresh_scores, name='refresh_scores'),
    path('scores/summary/', views.score_summary, name='score_summary'),
]