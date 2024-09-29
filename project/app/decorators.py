from django.http import HttpResponseForbidden
from functools import wraps
from django.shortcuts import render

def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        return render(request, "noPermission.html")
    return _wrapped_view
