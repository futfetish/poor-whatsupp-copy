from django.urls import path
from . import views, consumers

urlpatterns = [

    path('', views.main , name='home'),
    path('edit_name/<str:new_name>/', views.edit_name, name='edit_name'),
    path('avatar/', views.edit_ava, name='save_user_ava'),
    path('personal_msg/<int:pk>' , views.ls , name='ls'),
    path('search/' , views.search , name='search'),
    path('search2/' , views.search2 , name='search2'),
    path('create_msg' , views.create_msg , name='create_msg'),
    path('delete/msg/<int:msg_id>' , views.del_msg , name='delete_msg'),
    path('block/<int:prof_id>' , views.block , name='block'),
    path('msgs/<int:pk>', views.msgs.as_view(), name='msgs'),
    path('channel/<int:pk>', views.channel.as_view(), name='channel'),
]
