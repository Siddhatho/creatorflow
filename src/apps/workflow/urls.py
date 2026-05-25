from django.urls import path
from . import views

app_name = 'workflow'

urlpatterns = [
    path('', views.content_list, name='content_list'),
    path('create/', views.content_create, name='content_create'),
    path('<int:pk>/edit/', views.content_edit, name='content_edit'),
    path('<int:pk>/advance/', views.content_advance, name='content_advance'),
    path('<int:pk>/', views.content_detail, name='content_detail'),
    path('campaigns/', views.campaign_list, name='campaign_list'),
    path('campaigns/create/', views.campaign_create, name='campaign_create'),
    path('campaigns/<int:pk>/', views.campaign_detail, name='campaign_detail'),
    path('campaigns/<int:pk>/edit/', views.campaign_edit, name='campaign_edit'),
]