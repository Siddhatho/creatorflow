from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.users.decorators import manager_required, reviewer_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')

# test view — only admin can access
@manager_required
def admin_only_test(request):
    return render(request, 'core/home.html')


# test view — only reviewer/admin can access
@reviewer_required
def reviewer_only_test(request):
    return render(request, 'core/home.html')