from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class GroupRequiredMixin:
    groups = None

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied

        groups_set = set(self.groups or [])

        raw_groups = user.groups.all()
        user_groups = set([group.name for group in raw_groups])

        if not user_groups.intersection(groups_set) and \
                not user.is_superuser:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
