from django.urls import path
from . import views

app_name = 'ai_engine'

urlpatterns = [
    path('test/', views.ai_test, name='ai_test'),
    path('models/', views.ai_models, name='ai_models'),
]