from django.db.models import Q

from .models import C_user, Msg, Channel


def friend_list(request):
    if not request.user.is_authenticated:
        return {}
    related_users = C_user.objects.filter(
        Q(channel__in=Channel.objects.filter(members=request.user))
    ).exclude(id=request.user.id)
    return {'friend_list': related_users}