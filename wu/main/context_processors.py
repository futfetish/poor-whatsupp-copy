from django.db.models import Q

from .models import C_user , Msg


def friend_list(request):
    if not request.user.is_authenticated:
        return {}
    related_users = C_user.objects.filter(
        Q(sent__in=Msg.objects.filter(point=request.user)) | Q(point__in=Msg.objects.filter(sent=request.user))
    ).distinct()

    return {'friend_list': related_users}