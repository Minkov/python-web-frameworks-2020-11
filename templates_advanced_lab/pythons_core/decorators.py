from django.http import HttpResponse


def group_required(groups=[]):
    groups_set = set(groups)

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            # raw_groups = request.user.groups.only('name')
            raw_groups = request.user.groups.all()
            user_groups = set([group.name for group in raw_groups])

            if user_groups.intersection(groups_set):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized')

        return wrapper

    return decorator
