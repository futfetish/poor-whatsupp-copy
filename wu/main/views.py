from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from PIL import Image
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .forms import regform, CustomAuthForm
import os

from django.conf import settings

from .models import C_user, Msg


def main(request):
    return render(request , 'wu/home.html')

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
    return render(request , 'wu/reg.html' , {'form':form})

def login_(request):
    return render(request,'wu/login.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthForm
    template_name = 'wu/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

@login_required
def edit_name(request, new_name):

    request.user.username = new_name
    request.user.save()

    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def edit_ava(request):
    if request.method == 'POST' and request.FILES['image']:
        user = request.user
        image = request.FILES['image']
        user.ava = image
        user.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))

@method_decorator(login_required, name='dispatch')
class ls(DetailView):
    model = C_user
    template_name = 'wu/ls.html'
    context_object_name = 'prof'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Msg.objects.filter(Q(point=self.request.user.id, sent=context['prof']) | Q(point=context['prof'],sent=self.request.user)).order_by('date')
        return context

@login_required
def search(request):
    query = request.GET.get('q', '')
    select_users = C_user.objects.filter( username__icontains=query) if query else []
    context = {'select_users': select_users, 'query': query}
    return render(request, 'wu/search.html', context)

@login_required
def create_msg(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        point_id = request.POST.get('point')
        point = C_user.objects.get(id=point_id)
        if not point.blacklist.filter(id=request.user.id).exists() and text.strip():
            Msg.objects.create(sent=request.user, point=point, text=text)


        return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def search2(request):
    query = request.GET.get('q', '')

    select_users = C_user.objects.filter(
        Q(sent__in=Msg.objects.filter(point=request.user)) | Q(point__in=Msg.objects.filter(sent=request.user))
    ).distinct().filter( username__icontains=query) if query else C_user.objects.filter(
        Q(sent__in=Msg.objects.filter(point=request.user)) | Q(point__in=Msg.objects.filter(sent=request.user))
    ).distinct()

    context = {'select_users': select_users, 'query': query}
    return render (request, 'wu/search.html', context)

@login_required
def del_msg(request , msg_id):
    msg = Msg.objects.get(id=msg_id)
    if msg.sent != request.user:
        return redirect(request.META.get('HTTP_REFERER'))
    msg.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def block(request , prof_id):
    user = C_user.objects.get(id=prof_id)
    if user not in request.user.blacklist.all():
        request.user.blacklist.add(user)
    else:
        request.user.blacklist.remove(user)
    return redirect(request.META.get('HTTP_REFERER'))

class msgs(DetailView):
    model = C_user
    template_name = 'wu/msgs.html'
    context_object_name = 'prof'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Msg.objects.filter(Q(point=self.request.user.id, sent=context['prof']) | Q(point=context['prof'],sent=self.request.user)).order_by('date')
        return context