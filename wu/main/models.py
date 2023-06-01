from django.contrib.auth.models import AbstractUser

from django.db import models

class C_user(AbstractUser):
    ava = models.ImageField(default= 'main/static/wu/img/def_anime_ava.png',upload_to='main/static/wu/img/')
    blacklist = models.ManyToManyField('self',  blank=True,  symmetrical=False)
class Msg(models.Model):
    sent = models.ForeignKey(C_user, on_delete=models.CASCADE, related_name='sent')
    point = models.ForeignKey(C_user , on_delete=models.CASCADE, related_name='point')
    text = models.TextField(max_length= 20000)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
