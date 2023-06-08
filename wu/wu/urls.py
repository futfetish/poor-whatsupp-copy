from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from channels.routing import ProtocolTypeRouter, URLRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('authf/',include('authf.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

