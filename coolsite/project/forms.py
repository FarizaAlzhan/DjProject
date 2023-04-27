from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import *

class AddTraining1Form(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Название")
    time = forms.CharField(max_length=255, label="Время")
    place = forms.CharField(max_length=255, label="Место")
    training_manager = forms.CharField(max_length=255, label="Спикер")
    class Meta:
        model = Training1
        fields = ['title','time','place','training_manager','photo']

class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля',widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username','email',   'password1','password2']

class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-input mt-1'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя',max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Отзыв')
    captcha = CaptchaField(label='Введите текст из картинки:')


class AddEnrollForm(forms.ModelForm):
    full_name = forms.CharField(max_length=255, label="Фио")
    age = forms.CharField(max_length=255, label="Возраст")
    address = forms.CharField(max_length=255, label="Адресс")
    number = forms.CharField(max_length=255, label="Номер")
    class Meta:
        model = Enroll
        fields = ['full_name' ,'age','address','number']
