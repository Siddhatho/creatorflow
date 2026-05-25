from django.core.exceptions import PermissionDenied
from functools import wraps


def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                from django.shortcuts import redirect
                return redirect('login')
            if request.user.role not in roles:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def creator_required(view_func):
    return role_required('creator', 'admin')(view_func)


def reviewer_required(view_func):
    return role_required('reviewer', 'admin')(view_func)


def manager_required(view_func):
    return role_required('admin')(view_func)