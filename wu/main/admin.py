from django.contrib import admin
from .models import C_user , Msg , Channel

admin.site.register(C_user)
admin.site.register(Msg)
admin.site.register(Channel)
# Register your models here.
