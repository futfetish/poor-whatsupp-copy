from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import regform, CustomAuthForm


# Create your views here.
def lout (request):
    logout(request)
    return redirect('home')
def reg(request):
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            C_user = form.save()
            login(request, C_user)
            return redirect('home')
    else:
        form = regform()
    return render(request , 'auth/reg.html' , {'form':form})

def login_(request):
    return render(request,'auth/login.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthForm
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
