
from django.urls import path
from . import views

urlpatterns = [
    path('lout/', views.lout, name='lout'),
    path('reg/', views.reg, name='reg'),
    path('login/', views.CustomLoginView.as_view(template_name='auth/login.html'), name='login_'),
]
