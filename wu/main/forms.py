from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import TextInput
from .models import C_user

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'input__', 'placeholder': 'Имя пользователя' , 'style' : 'width :100%; margin-top:10px;'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class': 'input__', 'placeholder': 'Пароль' , 'style' : 'width :100%; margin-top:10px;'}))


class regform(UserCreationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class' : 'input__','placeholder': 'имя пользователя', 'style' : 'width :100%; margin-top:10px; '}))
    password1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input__', 'placeholder': 'пароль' , 'style' : 'width :100%;  margin-top:10px;'}))
    password2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input__', 'placeholder': 'повтор пароля' , 'style' : 'width :100%;  margin-top:10px;'}))
    class Meta:
        model = C_user
        fields = (
            'username',
            'password1',
            'password2'
        )
        widgets = {
            'username': TextInput(attrs={
                'class': 'input',
                'placeholder': 'имя пользователя'
            }),
            'password1': TextInput(attrs={
                'class': 'input ',
                'placeholder': 'пароль'
            }),
            'password2': TextInput(attrs={
                'class': 'input ',
                'placeholder': 'пароль'
            })
        }