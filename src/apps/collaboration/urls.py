from django.urls import path
from . import views

app_name = 'collaboration'

urlpatterns = [
    path('comment/<int:content_id>/', views.add_comment, name='add_comment'),
    path('review/<int:content_id>/', views.review_content, name='review_content'),
]