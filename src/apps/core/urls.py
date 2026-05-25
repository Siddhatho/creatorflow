from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/admin/', views.admin_only_test, name='test_admin'),
    path('test/reviewer/', views.reviewer_only_test, name='test_reviewer'),
]