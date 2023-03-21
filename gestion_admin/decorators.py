from django.shortcuts import redirect



def for_admin(view_func, *args, **kwargs):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='admin').exists():
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home')
    return wrapper_func
