from django.shortcuts import redirect





def yes_connect(view_func, *args, **kwargs):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def for_user(view_func, *args, **kwargs):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.all()[0].name == 'admin' and request.user.is_authenticated:
                return redirect('profiles', n=0)
            else:
                return view_func(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func